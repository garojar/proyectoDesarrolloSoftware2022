from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
)
from petclub.models import (
    Pet,
    Person,
)
from petclub.serializers import (
    PetModelSerializer,
    PersonCustomSerializer,
    PersonSerializer,
)


class HelloWorld(APIView):
    def get(self, request):
        return Response(data="Hola gente estoy en el get", status=200)

    def patch(self, request):
        return Response(data="Hola gente estoy en el patch", status=200)

    def delete(self, request):
        return Response(data="Hola gente estoy en el delete", status=200)

    def post(self, request):
        return Response(data="Hola gente estoy en el post", status=200)

class PetAPIView(APIView):

    def get(self, request, *args, **kwargs):
        pets = Pet.objects.all()
        serializer = PetModelSerializer(pets,many=True)
        return Response(data=serializer.data, status=200)

    def post(self, request):
        pass

    def patch(self, request):
        return Response(data="", status=200)


class PersonAPIView(APIView):

    def post(self, request):
        serializer = PersonCustomSerializer(data=request.data)

        if serializer.is_valid():
            # Caso exitoso
            validated_data = serializer.validated_data
            new_person = Person.objects.create(**validated_data)

            status_code = status.HTTP_200_OK
            data = PersonSerializer(new_person).data
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            data = {'error': str(serializer.errors)}

        return Response(data=data, status=status_code)

    def get(self, request):
        pass