from django.contrib.auth.models import User
from django.db import models

from helpers.app_defaults import integration_status_code, conversion_trigger_types
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


class DefaultEvent(AppBaseModel):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Product(AppBaseModel):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Offer(AppBaseModel):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                null=True, blank=True)
    name = models.CharField(max_length=55)
    trigger_type = models.CharField(max_length=30,
                                    choices=conversion_trigger_types,
                                    default='on-page-load')
    offer_value = models.FloatField()

    def __str__(self):
        return self.name


class MonitoredEventLog(AppBaseModel):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE)
    default_event = models.ForeignKey(DefaultEvent,
                                      on_delete=models.CASCADE, blank=True
                                      , null=True)
    conversion_offer = models.ForeignKey(Offer,
                                         on_delete=models.CASCADE,
                                         null=True)
    log_value = models.CharField(max_length=140, null=True, blank=True)
    log_extra_data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return
