""" views """
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication


from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            "Uses actions (list, create, retrieve, update, partial_update)",
            "Automatically maps to URLs using Routers",
            "Provides more functionality with less code",
        ]

        return Response({"message": "Hello!", "a_viewset": a_viewset})

    def retrieve(self, request, pk=None):
        """handle getting object by id"""
        return Response({"http_method": "GET"})

    def create(self, request):
        """Create a new Hello message"""
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            name = serializers.validated_data.get("name")
            message = f"Hello {name}!"
            return Response({"message": message})
        else:
            return Response(
                serializers.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def update(self, request, pk=None):
        """Handle updating full object"""
        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """Handle updating a part of an object"""
        return Response({"http_method": "PATCH"})

    def destroy(self, request, pk=None):
        """Handle removing a object"""
        return Response({"http_method": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
