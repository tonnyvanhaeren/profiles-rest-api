from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializers a name field fot testing our APIView"""

    name = serializers.CharField(max_length=10)
