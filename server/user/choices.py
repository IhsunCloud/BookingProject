from django.db.models import TextChoices


class Gender(TextChoices):
    FEMALE = 'F', ('FEMALE')
    MALE   = 'M', ('MALE')
    OTHER  = 'O', ('OTHER')