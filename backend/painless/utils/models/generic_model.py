from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class GenericModel(models.Model):
	"""
	Abstract model for generic content types.
	"""
	content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE, db_index = True)
	object_id    = models.PositiveIntegerField(db_index = True)
	content_object = GenericForeignKey('content_type', 'object_id')

	class Meta:
		abstract = True