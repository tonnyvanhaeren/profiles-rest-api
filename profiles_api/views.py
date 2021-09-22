""" views """
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, fomat=None):
        """Returns a list of API features"""
        an_apiview = [
            "Uses HTTP Methods as function (get, post, patch, put, delete)",
            "Is simultar to a tradition Django view",
            "Gives you the most controll over you application logic",
            "Is mapped manually to URLs",
        ]

        return Response({"message": "hello", "an_apiview": an_apiview})
