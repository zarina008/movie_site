from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    phone_number = PhoneNumberField(region='KG', default='+996')
    profile_image = models.ImageField(upload_to='profile_images/',null=True, blank=True)
    STATUS_CHOICES = (
    ('pro', 'pro'),
    ('simple', 'simple')
    )
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='simple')

class Director(models.Model):
    director_name = models.CharField(max_length=32)
    bio = models.TextField(null=True, blank=True)
    director_image =models.ImageField(upload_to='director_images/')

class Actor(models.Model):
     actor_name = models.CharField(max_length=32)
     bio = models.TextField(null=True, blank=True)
     actor_image = models.ImageField(upload_to='actor')

class Genre(models.Model):
     genre_name = models.CharField(max_length=32, unique=True)

class Country(models.Model):
    country_name = models.CharField(max_length=32, unique=True)

class Movie(models.Model):
    movie_name = models.CharField(max_length=32)
    movie_image =models.ImageField(upload_to='movie_image/')
    movie_trailer = models.FileField(upload_to='movie_trailer/')
    release_date = models.DateField()
    country = models.ManyToManyField(Country)
    director = models.ManyToManyField(Director)
    genre = models.ManyToManyField(Genre)
    TYPE_QIALITI = (
        ('360', '360'),
        ('480','480'),
        ('720', '720'),
        ('1080', '1080')
    )
    type_qialiti = models.CharField(max_length=5, choices=TYPE_QIALITI)
    time_movie = models.PositiveSmallIntegerField(default=0)
    actors = models.ManyToManyField(Actor)
    description = models.TextField(null=True, blank=True)

class MovieLanguage(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie_Language_name = models.CharField(max_length=32)
    video_movie = models.FileField(upload_to='video_movies')

class MovieMoments(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    moments_image = models.ImageField(upload_to='moments_image',null=True, blank=True)
    moment_videos = models.FileField(upload_to='moment_video/',null=True, blank=True)

class Review(models.Model):
    user = models.ForeignKey(UserProfile)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comments = models.TextField(null=True, blank=True)
    start =  models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 11)], null=True, blank=True)


class Favorite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)







