from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView

from bigpixel.selectors import fetch_product_offer_by_name
from bigpixel.serializers import InputOfferSerializer, OutputOfferSerializer
from bigpixel.services import create_offer


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


# create offer
class CreateOfferApi(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, **kwargs):
        serializer = InputOfferSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        offer = create_offer(**serializer.validated_data, owner=request.user)

        survey_serializer_data = OutputOfferSerializer(offer)

        return Response(data={
            'data': survey_serializer_data.data,
        }, status=HTTP_201_CREATED)
