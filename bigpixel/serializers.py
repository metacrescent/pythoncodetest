from rest_framework import serializers

from bigpixel.models import Offer


class InputOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('trigger_type',
                  'name',
                  'offer_value',)


class OutputOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('owner',
                  'product',
                  'name',
                  'trigger_type',
                  'offer_value',
                  'status',
                  'created_at',
                  'updated_at')
