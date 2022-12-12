from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Model definition of User.
    """
    first_name = models.CharField(
        _('First Name'),
        max_length = 16
    )

    last_name = models.CharField(
        _('Last Name'),
        max_length = 16
    )
    
    surname = models.CharField(
        _('Surname'),
        max_length = 16
    )
    
    phone_number = models.CharField(
        _('Phone Number'),
        max_length = 16,
        unique = True,
        blank  = False,
    )
    
    otp = models.CharField(
        _('OTP'),
        max_length = 6,
        help_text  = _('One Time Password. e.g.: 101010')
    )
    
    birthday = models.DateField(
        _('Birthday'),
        auto_now_add=True
    )
    
    gender = models.CharField(
        _('Gender'),
        # choices = ,
        max_length = 2
    )
    
    nationality = models.CharField(
        _('Nationality'),
        max_length = 16
    )
    
    passport_code = models.CharField(
        _('Passport Code'),
        max_length = 16
    )
    
    country = models.CharField(
        _('Country'),
        max_length = 16
    )
    
    city = models.CharField(
        _('City'),
        max_length = 16
    )
    
    address = models.TextField(
        _('Address'),
    )
    
    zip_code = models.CharField(
        _('Zip Code'),
        max_length = 16
    )
    
    class Meta:
        """
        Meta definition of User.
        """
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        """ String representation of User."""
        return '{self.first_name}.{self.last_name} ~ {self.phone}'

    def __repr__(self):
        """ String representation of User."""
        return self.__str__()