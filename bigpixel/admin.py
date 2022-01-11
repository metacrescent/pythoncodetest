from django.contrib import admin

from bigpixel.models import PixelTrackingCode, PixelTrackingCodeSite, Product, Offer, MonitoredEventLog


@admin.register(PixelTrackingCode)
class PixelTrackingCodeAdmin(admin.ModelAdmin):
    pass


@admin.register(PixelTrackingCodeSite)
class PixelTrackingCodeSiteAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    pass


@admin.register(MonitoredEventLog)
class MonitoredEventLogAdmin(admin.ModelAdmin):
    pass
