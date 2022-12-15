from django.db import models
from django.utils.translation import gettext_lazy as _

from hotel.managers import ReviewManager
from painless.models import (
    SluggedModel,
    TimeStampedModel
)


class Reviews(SluggedModel, TimeStampedModel):
	"""
    Model definition for Reviews.

    Args:
		fullname (str): name of the author
		is_active (bool): is the review active
		rating (int): rating of the review
		text (str): text of the review
		featured (bool): is the review is helpful
    """
	fullname = models.CharField(
		_('Fullname'),
  		max_length = 50
    )

	is_active = models.BooleanField(
    	_('Review Activity'),
     	default = False
    )

	rating = models.IntegerField(
    	_('Review Rating'),
    	default = 0
    )

	text = models.TextField(
		_('Review Text'),
  		max_length = 256
  	)

	featured = models.BooleanField(
		_('Featured Review'),
		default = False,
		help_text = _('Is this review is helpful to users? e.g: `False`')
	)

	class Meta:
		""" Meta definition for Comment. """
		ordering = ['-created_at']
		verbose_name = _('Review')
		verbose_name_plural = _('Reviews')

	def __str__(self):
		""" Unicode representation of Comments. """
		return 'Review {self.text} by {self.fullname}.'

	def __repr__(self):
		""" Unicode representation of Comments. """
		return self.__str__()

	objects = ReviewManager()