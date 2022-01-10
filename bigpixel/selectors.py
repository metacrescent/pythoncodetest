from django.shortcuts import get_object_or_404

from bigpixel.models import PixelTrackingCode


# check if user's pixel tracking code already exists
def pixel_tracking_code_exists(user):
    return PixelTrackingCode.objects.filter(user=user).exists()


# fetch user's pixel tracking code
def fetch_pixel_tracking_code(user):
    return get_object_or_404(PixelTrackingCode, user=user)
