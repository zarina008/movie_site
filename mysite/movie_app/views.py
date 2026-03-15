from rest_framework import viewsets
from .models import (UserProfile, Country,
                     Director, Actor, Genre, Movie, MovieMoments,
                     MovieLanguage, Review,Favorite)
from .serializers import (UserProfileSerializers, CountrySerializers, DirectorSerializers,
                          ActorSerializers, GenreSerializers, MovieSerializers, MovieMomentsSerializers,
                          MovieLanguageSerializers, ReviewSerializers, FavoriteSerializers)



class UserProfileViewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class =UserProfileSerializers

    def creat(self, request, *args, **kwargs):

class CountryViewset(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class =CountrySerializers

class DirectorViewset(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class =DirectorSerializers

class ActorViewset(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class =ActorSerializers

class GenreViewset(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class =GenreSerializers

class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class =MovieSerializers

class MovieMomentsViewset(viewsets.ModelViewSet):
    queryset = MovieMoments.objects.all()
    serializer_class =MovieMomentsSerializers

class MovieLanguageViewset(viewsets.ModelViewSet):
    queryset = MovieLanguage.objects.all()
    serializer_class =MovieLanguageSerializers

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class =ReviewSerializers

class FavoriteViewset(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class =FavoriteSerializers
