from rest_framework import viewsets
from .models import (UserProfile, Country,
                     Director, Actor, Genre, Movie, MovieMoments,
                     MovieLanguage, Review,Favorite)


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__al__'


class DirectorSerializers(serializers.ModelSerializer):
            class Meta:
                model = Director
                fields = '__al__'

class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__al__'


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__al__'


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__al__'


class MovieMomentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieMoments
        fields = '__al__'


class MovieLanguageSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguage
        fields = '__al__'


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__al__'


class FavoriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__al__'

