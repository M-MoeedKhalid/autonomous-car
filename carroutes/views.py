import requests
from rest_framework import views, status
from rest_framework.response import Response

from carroutes.constants import URL
from carroutes.route_functions import car_route_result


class CarRoutes(views.APIView):

    def get(self, request, *args, **kwargs):
        """

        Hit this api to find if our autonomous car will be able to complete it's journey\n
        <br>Available parameters:

        <br>empty-route: To retrieve a route with empty track & travelLog arrays.

        <br>success-no-obstacles: To retrieve a successful track with no obstacles.

        <br>success-with-obstacles: To retrieve a successful track with obstacles.

        <br>failure-out-of-bounds: To retrieve a route that should result in failure due to running out of bounds.

        <br>failure-hits-obstacle: To retrieve a route that should result in failure due to running into an obstacle.

        <br>random: To retrieve a random route including the empty route.

        """
        response = ""
        try:
            # Hit our API
            url = URL + f"{kwargs['route']}"
            response = requests.get(url)

            # Store response into respective variables
            route = response.json()['route']
            track = route['track']
            travel_log = route['travelLog']

            return Response(car_route_result(track, travel_log))
        except KeyError:
            return Response(response.json())


class Error404(views.APIView):
    def get(self, request, *args, **kwargs):
        return Response({"errors": [{"code": "NOT_FOUND", "field": "", "message": "That url was not found"}]})
