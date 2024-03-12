from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name=models.CharField(max_length=20)
    cuisine=models.CharField(max_length=30)
    mealtype=models.CharField(max_length=30)
    ingredients=models.TextField()
    desc=models.TextField()
    recipe_preparation_time=models.TimeField()
    image = models.ImageField(upload_to="images", null=True, blank=True)



    def __str__(self):
        return self.recipe_name

class Rating(models.Model):
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    review=models.TextField()
    rating=models.PositiveIntegerField(choices=((1,'1 star'),(2,'2 star'),(3,'3 star'),(4,'4 star'),(5,'5 star')))
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.review








