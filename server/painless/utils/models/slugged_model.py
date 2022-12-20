from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from painless.fields import USField


class SluggedModel(models.Model):
	"""
	Model definition of General Model.
	"""
	title = models.CharField(
		_('Title'),
		max_length = 255
	)

	slug = models.SlugField(
		_('Slug'),
		max_length = 255,
		db_index   = True,
		unique = True,
		blank  = True
	)

	class Meta:
		""" Meta information of General Model. """
		abstract = True
		ordering = ('title',)
		verbose_name = _('Slugged Model')
		verbose_name_plural = _('Slugged Models')

	def __str__(self):
		""" String representation of Slugged Model. """
		return self.title

	def __repr__(self):
		""" String representation of Slugged Model. """
		return self.__str__()

	def __unicode__(self):
		""" String representation of Slugged Model. """
		return self.title

	def clean(self):
		from django.core.exceptions import ValidationError

		if self.title:
			slug = self.get_slug()
		else:
			raise ValidationError(
       			'Please enter a valid title/name. \
            	It must contain at least one character.')

	def get_slug(self):
		""" Allows subclasses to implement their own slug creation logic. """
		slug = ''

		# If title is None, slugify returns 'none' as string.
		if self.title is not None:
			slug = slugify(self.title)

		# For titles like `!@#$!@#$`, slugify returns an empty string.
		if slug == '':
			slug = str(USField)[:7]
		return slug[:256]

	def save(self, *args, **kwargs):
		""" Create a unique slug by appending an index. """
		update_slug = kwargs.pop('update_slug', False)

		new_slug = False
		if not self.slug or update_slug:
			new_slug = True

		if new_slug:
		  self.slug = self.get_slug()