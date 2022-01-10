from django.contrib.auth.models import User
from django.db import models

from helpers.app_defaults import integration_status_code
from helpers.generators import alphanumerical_generator
from helpers.models import AppBaseModel


class PixelTrackingCode(AppBaseModel):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    tracking_code = models.CharField(max_length=16,
                                     unique=True)
    tracking_code_status = models.CharField(max_length=30, default='unreachable')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = alphanumerical_generator(16)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tracking_code


class PixelTrackingCodeSite(AppBaseModel):
    tracking_code = models.ForeignKey(PixelTrackingCode,
                                      on_delete=models.CASCADE)
    website = models.URLField(max_length=55,
                              unique=True)
    integration_status = models.CharField(max_length=30,
                                          choices=integration_status_code,
                                          default='unreachable')

    def __str__(self):
        return self.website
