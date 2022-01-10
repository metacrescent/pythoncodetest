from django.contrib import admin

from bigpixel.models import PixelTrackingCode, PixelTrackingCodeSite


@admin.register(PixelTrackingCode)
class PixelTrackingCodeAdmin(admin.ModelAdmin):
    pass


@admin.register(PixelTrackingCodeSite)
class PixelTrackingCodeSiteAdmin(admin.ModelAdmin):
    pass
