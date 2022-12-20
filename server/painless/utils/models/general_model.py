from painless.fields import UserField, USField
from .slugged_model import SluggedModel
from .timestamped_model import TimeStampedModel


class GeneralModel(SluggedModel, TimeStampedModel):
    """
    An abstract base class model.

    Args:
        - title (str):
            The title of the model.
        - slug (str):
            The unique slug of the model.
        - timestamped (datetime):
            Provides the `created_at`, `deleted_at`, `trashed_at`, `updated_at` fields.
        - us_id (str):
            The yusef-id of the object.
        - user (fk):
            The user belongs to the object.
    """
    us_id = USField()
    user  = UserField()

    class Meta:
        abstract = True
