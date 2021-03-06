import uuid, os

from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def get_data_upload_to(instance, filename=None):
  path = 'data_uploads/{}'.format(instance.data_upload_uuid)

  if filename is not None:
    path += '/{}'.format(filename)

  return path

def import_document_validator(document):
  pass

class Prediction(models.Model):

  data_upload = models.FileField(upload_to=get_data_upload_to,
                                 validators=[import_document_validator])
  data_upload_uuid = models.CharField(max_length=32)
  col_ts = models.CharField(max_length=255)
  col_val = models.CharField(max_length=255)
  ts_format = models.CharField(max_length=50)

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def get_media_dir(self, absolute_path=False):
    return os.path.join(
      settings.MEDIA_ROOT if absolute_path else settings.MEDIA_URL,
      get_data_upload_to(self)
    )

  def save(self, *args, **kwargs):
    if self.pk is None:
      self.data_upload_uuid = uuid.uuid4().hex

    super(Prediction, self).save(*args, **kwargs)

  def __str__(self):
    return 'Prediction - {}'.format(self.pk)

  class Meta:
    verbose_name = _('Prediction')
    verbose_name_plural = _('Predictions')
    ordering = [ '-updated' ]