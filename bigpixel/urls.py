from django.urls import path

from bigpixel.views import HomeView, GeneratePixelCodeView, ValidatePixelCodeIntegrationView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('generate-pixel-code/', GeneratePixelCodeView.as_view(), name='generate_pixel_code'),
    path('validate-pixel-code/', ValidatePixelCodeIntegrationView.as_view(), name='validate_pixel_code'),
]
