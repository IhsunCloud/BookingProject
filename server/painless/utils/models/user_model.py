from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _

from .address_model import AddressModel


class Gender(TextChoices):
    FEMALE = 'F', ('FEMALE')
    MALE   = 'M', ('MALE')
    OTHER  = 'O', ('OTHER')


class User(AbstractUser):
    phone_number = models.CharField(
        _('Phone Number'),
        max_length = 16,
        unique = True,
        blank  = False,
    )

    USERNAME_FIELD = "phone_number"


class Profile(models.Model):
    """
    Model definition of the User.

    Args:
        - first_name (str):
            firstname of the user.
        - last_name (str):
            lastname of the user.
        - phone_number (str):
            phonenumber of the user.
        - otp (str):
            one time password for the user logins.
        - birthday (datetime):
            birthdate of the user.
        - gender (str):
            gender of the user.
        - nationality (str):
            nationality of the.
        - passport_code (str):
            passport number of the user.
    """
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        verbose_name = _('User'),
        related_name = 'user_profiles',
    )

    first_name = models.CharField(
        _('First Name'),
        max_length = 16
    )

    last_name = models.CharField(
        _('Last Name'),
        max_length = 16
    )

    address = AddressModel(
        _('Address'),
    )

    otp = models.CharField(
        _('OTP'),
        max_length = 6,
        help_text  = _('One Time Password. e.g.: 101010')
    )

    birthday = models.DateField(
        _('Birthday'),
        auto_now_add = True
    )

    gender = models.CharField(
        _('Gender'),
        choices = Gender.choices,
        default = Gender.FEMALE,
        max_length = 2
    )

    nationality = models.CharField(
        _('Nationality'),
        max_length = 16
    )

    passport_code  = models.CharField(
        _('Passport Code'),
        max_length = 16
    )

    def __str__(self):
        """ String representation of User."""
        return f'{self.first_name}.{self.last_name} ~ {self.user.phone_number}'

    def __repr__(self):
        """ String representation of User."""
        return self.__str__()
