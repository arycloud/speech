import os
import random
import string
from pathlib import Path
from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponse
from django.http import FileResponse
from google.cloud import texttospeech_v1beta1

from Base import settings
from . import forms
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('svc_cred.json')


# credentials = GoogleCredentials.get_application_default()


def generate_pid():
    digits = "".join([random.choice(string.digits) for i in range(4)])
    pid = digits
    return pid


def text_to_speech_manager(text_path, pitch, speed, gender, type):
    text = text_path
    txt = Path(text_path).read_text(encoding='cp1252')
    input_text = {'text': txt}
    voice = {
        'language_code': 'en-US',
        'name': type,
        'ssml_gender': gender,
    }
    audio_config = {
        'audio_encoding': texttospeech_v1beta1.enums.AudioEncoding.MP3,
        'pitch': float(pitch),
        # 'speakingRate': speed,
    }
    client = texttospeech_v1beta1.TextToSpeechClient(credentials=credentials)
    response = client.synthesize_speech(input_=input_text,
                                        voice=voice,
                                        audio_config=audio_config)
    with open('media/audios/output.mp3', 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

    # dict_response = dict(response)
    response_file = FileResponse('media/audios/output.mp3', content_type='mp3')
    response_file['Content-Disposition'] = 'attachment; filename="output.mp3"'
    return response_file


class BaseView(CreateView):
    def get(self, request, *args, **kwargs):
        form = forms.BaseForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            post_data = request.POST.copy()
            form = forms.BaseForm(post_data, request.FILES)
            print('get post req')
            print(form.errors)
            if form.is_valid():
                print('form is valid')
                obj = form
                obj.textFile = form.cleaned_data['textFile']
                obj.gender = form.cleaned_data['gender']
                obj.pitch = form.cleaned_data['pitch']
                obj.speed = form.cleaned_data['speed']
                obj.voice_type = form.cleaned_data['voice_type']
                obj.save()
                text_path = os.path.join(settings.MEDIA_ROOT, 'texts/', obj.textFile.name)
                text = text_path
                txt = Path(text).read_text(encoding='cp1252')
                fileName = obj.textFile.name[:-4]
                print('File Name is: {}'.format(fileName))
                input_text = {'text': txt}
                voice = {
                    'language_code': 'en-US',
                    'ssml_gender': obj.gender,
                }
                audio_config = {
                    'audio_encoding': texttospeech_v1beta1.enums.AudioEncoding.MP3,
                    'pitch': float(obj.pitch),
                    'speaking_rate': float(obj.speed),
                }
                client = texttospeech_v1beta1.TextToSpeechClient(credentials=credentials)
                response = client.synthesize_speech(input_=input_text,
                                                    voice=voice,
                                                    audio_config=audio_config)
                with open('media/audios/' + str(fileName) + '.mp3', 'wb') as out:
                    out.write(response.audio_content)
                    print('Audio content written to file "output.mp3"')
                
                file = open('media/audios/' + str(fileName) + '.mp3', "rb").read()
                rea_response = HttpResponse(file, content_type='audio/mpeg')
                rea_response['Content-Disposition'] = 'attachment; filename={}'.format(fileName + '.mp3')

                return rea_response
            else:
                return HttpResponse('Something went wrong', status=400)

