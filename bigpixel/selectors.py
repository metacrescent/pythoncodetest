from django.shortcuts import get_object_or_404

from bigpixel.models import PixelTrackingCode, Product, Offer


# check if user's pixel tracking code already exists
def pixel_tracking_code_exists(user):
    return PixelTrackingCode.objects.filter(user=user).exists()


# fetch user's pixel tracking code
def fetch_pixel_tracking_code(user):
    return get_object_or_404(PixelTrackingCode, user=user)


# fetch user's product or offer
def fetch_product_offer_by_name(user, name):
    item_data = []
    products = Product.objects.filter(owner=user, name__icontains=name)
    offers = Offer.objects.filter(owner=user, name__icontains=name)

    for product in products:
        item_data.append(product.name)

    for offer in offers:
        item_data.append(offer.name)

    return item_data
