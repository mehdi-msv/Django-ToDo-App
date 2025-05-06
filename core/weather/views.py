import requests
from django.conf import settings
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import CityInputSerializer


class WeatherAPIView(APIView):
    @swagger_auto_schema(request_body=CityInputSerializer)
    def post(self, request):
        """
        Fetches the weather data for the given city and returns it.

        The given city is first checked in the cache. If the data is not in the cache,
        a request is sent to the OpenWeatherMap API to fetch the data. The response
        is then cached for 20 minutes.

        Parameters:
        - city (str): The city for which to fetch the weather data

        Returns:
        - Response: A response containing the weather data for the given city,
          or an error message and a 500 status code if the request failed.

        Example:
        >>> response = client.post('/api/weather/', {'city': 'Tehran'})

        :param request:
        :return:
        """
        serializer = CityInputSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        city = request.data.get("city")
        if not city:
            return Response(
                {"error": "city is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        cache_key = f"weather_{city.lower()}"
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        response = requests.get(
            settings.OPENWEATHER_URL,
            params={
                "q": city,
                "appid": settings.OPENWEATHER_API_KEY,
                "units": "metric",
                "lang": "fa",
            },
        )

        if response.status_code == 200:
            data = response.json()
            cache.set(cache_key, data, timeout=60 * 20)
            return Response(data)

        return Response(
            {"error": "failed to fetch weather"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    def get(self, request):
        """
        Return a message telling the user to enter a city.

        :param request:
        :return: A response containing the message and a 200 status code.
        """
        return Response(
            {"detail": "please enter your city"}, status=status.HTTP_200_OK
        )
