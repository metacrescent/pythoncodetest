from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from bigpixel.selectors import fetch_product_offer_by_name


@api_view(http_method_names=['GET'])
@permission_classes([IsAuthenticated, ])
def fetch_product_or_offer_by_name(request):
    name = request.GET.get('name')
    data = []
    if name:
        data = fetch_product_offer_by_name(user=request.user, name=name)
    return Response({
        'data': data
    })
