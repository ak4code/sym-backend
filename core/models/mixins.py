from django.db import models


class AutoTimestampMixin(models.Model):
    """Abstract model for auto-timestamping created_at and updated_at fields"""

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        abstract = True
