from rest_framework import serializers


class CityInputSerializer(serializers.Serializer):
    """
    A serializer to validate the city input.
    """

    city = serializers.CharField(required=True, max_length=100)
