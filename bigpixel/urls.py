from django.urls import path

from bigpixel.api import fetch_product_or_offer_by_name, CreateOfferApi
from bigpixel.views import HomeView, GeneratePixelCodeView, ValidatePixelCodeIntegrationView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('generate-pixel-code/', GeneratePixelCodeView.as_view(), name='generate_pixel_code'),
    path('validate-pixel-code/', ValidatePixelCodeIntegrationView.as_view(), name='validate_pixel_code'),

    path('fetch-products-offer/', fetch_product_or_offer_by_name),
    path('create-offer/', CreateOfferApi.as_view()),
]
