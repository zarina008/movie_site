from django.contrib import admin
from .models import (UserProfile, Country,
                     Director, Actor, Genre, Movie, MovieMoments,
                     MovieLanguage, Review,Favorite)

admin.site.register(UserProfile)
admin.site.register(Country)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieLanguage)
admin.site.register(MovieMoments)
admin.site.register(Review)
admin.site.register(Favorite)