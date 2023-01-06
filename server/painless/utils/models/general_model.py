from django.utils.translation import gettext_lazy as _

from painless.utils.models.model_utils.fields import USField
from painless.utils.models.slugged_model import SluggedModel
from painless.utils.models.timestamped_model import TimeStampedModel
from painless.utils.models.user_model import User


class GeneralModel(SluggedModel, TimeStampedModel):
    """
    An abstract base class model.
    -----------------------------

    Arguments:
    ----------
        - title (str): The title of this model.
        ---------------------------------------
        - slug (str): The unique slug of this model.
        --------------------------------------------
        - timestamped (datetime):
          Provides the `created_at`, `deleted_at`, `trashed_at`, `updated_at` fields.
        --------------------------------------------------------------------------
        - us_id (uuid):
          The yusef-id of this object.
        ------------------------------
        - user (fk):
          The user belongs to this object.
        ----------------------------------
    """
    us_id = USField(
      _('Yusef ID'),
    )

    class Meta:
        abstract = True
