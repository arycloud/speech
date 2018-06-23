from django.db import models
from app.storage import OverwriteStorage


genders = (
    ('UNSPECIFIED', 'SSML_VOICE_GENDER_UNSPECIFIED'),
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
    ('NEUTRAL', 'NEUTRAL'),
)

voice_types = (
    ('nl-NL-Standard-A', 'nl-NL-Standard-A'),
    ('en-AU-Standard-A', 'en-AU-Standard-A'),
    ('en-AU-Standard-B', 'en-AU-Standard-B'),
    ('en-AU-Standard-C', 'en-AU-Standard-C'),
    ('en-AU-Standard-D', 'en-AU-Standard-D'),
    ('en-GB-Standard-A', 'en-GB-Standard-A'),
    ('en-GB-Standard-B', 'en-GB-Standard-B'),
    ('en-GB-Standard-C', 'en-GB-Standard-C'),
    ('en-GB-Standard-D', 'en-GB-Standard-D'),
    ('en-US-Wavenet-A', 'en-US-Wavenet-A'),
    ('en-US-Wavenet-B', 'en-US-Wavenet-B'),
    ('en-US-Wavenet-C', 'en-US-Wavenet-C'),
    ('en-US-Wavenet-D', 'en-US-Wavenet-D'),
    ('en-US-Wavenet-E', 'en-US-Wavenet-E'),
    ('en-US-Wavenet-F', 'en-US-Wavenet-F'),
    ('en-US-Standard-B', 'en-US-Standard-B'),
    ('en-US-Standard-C', 'en-US-Standard-C'),
    ('en-US-Standard-D', 'en-US-Standard-D'),
    ('en-US-Standard-E', 'en-US-Standard-E'),
    ('fr-FR-Standard-C', 'fr-FR-Standard-C'),
    ('fr-FR-Standard-D', 'fr-FR-Standard-D'),
    ('fr-CA-Standard-A', 'fr-CA-Standard-A'),
    ('fr-CA-Standard-B', 'fr-CA-Standard-B'),
    ('fr-CA-Standard-C', 'fr-CA-Standard-C'),
    ('fr-CA-Standard-D', 'fr-CA-Standard-D'),
    ('de-DE-Standard-A', 'de-DE-Standard-A'),
    ('de-DE-Standard-B', 'de-DE-Standard-B'),
    ('it-IT-Standard-A', 'it-IT-Standard-A'),
    ('ja-JP-Standard-A', 'ja-JP-Standard-A'),
    ('ko-KR-Standard-A', 'ko-KR-Standard-A'),
    ('pt-BR-Standard-A', 'pt-BR-Standard-A'),
    ('es-ES-Standard-A', 'es-ES-Standard-A'),
    ('sv-SE-Standard-A', 'sv-SE-Standard-A'),
    ('tr-TR-Standard-A', 'tr-TR-Standard-A'),
)

speed = (
    ('0.25', '0.25'),
    ('0.50', '0.50'),
    ('0.75', '0.75'),
    ('1', '1'),
    ('1.25', '1.25'),
    ('1.50', '1.50'),
    ('1.75', '1.55'),
    ('2', '2'),
    ('2.25', '2.25'),
    ('2.50', '2.50'),
    ('2.45', '2.75'),
    ('3', '3'),
    ('3.25', '3.25'),
    ('3.50', '3.50'),
    ('3.75', '3.75'),
    ('4', '4'),
)

pitch = (
    ('-20', '-20'),
    ('-19', '-19'),
    ('-18', '-18'),
    ('-17', '-17'),
    ('-16', '-16'),
    ('-15', '-15'),
    ('-14', '-14'),
    ('-13', '-13'),
    ('-12', '-12'),
    ('-11', '-11'),
    ('-10', '-10'),
    ('-09', '-09'),
    ('-08', '-08'),
    ('-07', '-07'),
    ('-06', '-06'),
    ('-05', '-05'),
    ('-04', '-04'),
    ('-03', '-03'),
    ('-02', '-02'),
    ('-01', '-01'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
)


class BaseModel(models.Model):
    textFile = models.FileField(storage=OverwriteStorage(), upload_to='texts/', name='textFile')
    gender = models.CharField(max_length=100, choices=genders, name='gender',)
    pitch = models.CharField(max_length=100, name='pitch', choices=pitch,)
    speed = models.CharField(max_length=100, name='speed', choices=speed,)
    voice_type = models.CharField(max_length=100, choices=voice_types, name='voice_type', default='')
