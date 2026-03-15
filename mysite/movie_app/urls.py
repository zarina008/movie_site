from django.urls import path, include
from rest_framework import routers
from .views import (UserProfileViewset, CountryViewset, DirectorViewset, ActorViewset,
                    GenreViewset, MovieViewset, MovieMomentsViewset, MovieLanguageViewset,
                    ReviewViewset, FavoriteViewset)

router = routers.DefaultRouter()

router.register( r'user_profile', UserProfileViewset, basename='user_profile')
router.register( r'country', CountryViewset, basename='country')
router.register( r'director', DirectorViewset, basename='director')
router.register( r'actor', ActorViewset, basename='actor')
router.register( r'genre', GenreViewset, basename='genre')
router.register( r'movie', MovieViewset, basename='movie')
router.register( r'movie_moments', MovieMomentsViewset, basename='movie_moments')
router.register( r'movie_language', MovieLanguageViewset, basename='movie_language')
router.register( r'review', ReviewViewset, basename='review')
router.register( r'favorite', FavoriteViewset, basename='favorite')






