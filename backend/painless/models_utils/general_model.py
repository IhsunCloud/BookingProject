from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class GeneralModel(models.Model):
    """
    Model definition of General Model.
    """
    title = models.CharField(
        _('Title'),
        max_length = 128,
    )
    slug  = models.SlugField(
        _('Slug'),
        unique = True,
        max_length = 128,
        allow_unicode = True,
    )
    
    class Meta:
        """
        Meta information of General Model.
        """
        abstract = True
        verbose_name = _('General Model')
        verbose_name_plural = _('General Models')
    
    def save(self, *args, **kwargs):
        """
        Slugify the title.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super(GeneralModel, self).save(*args, **kwargs)