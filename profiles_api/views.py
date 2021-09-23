""" views """
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, fomat=None):
        """Returns a list of API features"""
        an_apiview = [
            "Uses HTTP Methods as function (get, post, patch, put, delete)",
            "Is simultar to a tradition Django view",
            "Gives you the most controll over you application logic",
            "Is mapped manually to URLs",
        ]

        return Response({"message": "hello", "an_apiview": an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            name = serializers.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message": message})
        else:
            return Response(
                serializers.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, pk=None):
        """Handle updating an full object"""
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """Handle updating a partial of the object"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """Handle delete a object"""
        return Response({"method": "DELETE"})
