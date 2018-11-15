from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Advert
from .serializers import AdvertModelSerialier, UserModelSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics


@api_view(['GET', 'POST'])
def advert_list(request):
    if request.method == 'GET':
        adverts = Advert.objects.all()
        for ad in adverts:
            ad.number_of_views = ad.number_of_views + 1
            ad.save()
        serializer = AdvertModelSerialier(adverts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = AdvertModelSerialier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def advert_detail(request, pk):
    try:
        advert = Advert.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        advert.number_of_views = advert.number_of_views + 1
        advert.save()
        serializer = AdvertModelSerialier(advert)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = AdvertModelSerialier(advert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        advert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdvertList(APIView):

    def get(self, request):
        # request.header
        # token = Token.objects.get()
        # print(TokenAuthentication.authenticate_credentials(To))
        print(request.header)
        adverts = Advert.objects.all()
        for ad in adverts:
            ad.number_of_views = ad.number_of_views + 1
            ad.save()
        serializer = AdvertModelSerialier(adverts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AdvertModelSerialier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdvertDetail(APIView):

    def get_object(self, pk):
        try:
            return Advert.objects.get(id=pk)
        except:
            raise Http404

    def get(self, request, pk):
        advert = self.get_object(pk)
        advert.number_of_views = advert.number_of_views + 1
        advert.save()
        serializer = AdvertModelSerialier(advert)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        advert = self.get_object(pk)
        serializer = AdvertModelSerialier(advert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        advert = self.get_object(pk)
        advert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'Invalid'})
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})


@api_view(['POST'])
def register(request):
    serializer = UserModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)