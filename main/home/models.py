from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class BaseSettings(models.Model):
  phone = models.CharField(max_length=50, blank=True, null=True, db_index=True)
