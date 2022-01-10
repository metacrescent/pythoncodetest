from django.db import models

from helpers.generators import number_generator


class AppBaseModel(models.Model):
    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    slug = models.SlugField(null=True, db_index=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = number_generator(10)
        super().save(*args, **kwargs)
