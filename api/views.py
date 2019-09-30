from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Movie, Rating
from .serializers import MovieSerializers, RatingSerializers
# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:    

            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            print("user", user)

            response = {'message': 'its working'}
            return Response(response, status=status.HTTP_200_OK)
        else:
             response = {'message': 'You need to provide stars'}
             return Response(response, status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers