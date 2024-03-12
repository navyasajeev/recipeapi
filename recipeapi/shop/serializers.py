from django.contrib.auth.models import User
from rest_framework import serializers

from shop.models import Recipe

from shop.models import Rating


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields=['id','recipe_name','cuisine','mealtype','ingredients','desc','recipe_preparation_time','image']

class UserSerializer(serializers.ModelSerializer):
        password = serializers.CharField(write_only=True)

        class Meta:
            model = User
            fields = ['id', 'username', 'password']

        def create(self, validated_data):
            u = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
            u.save()
            return u


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id","recipe", "user","rating", "review"]



# class ReviewSerializer(serializers.ModelSerializer):
#     recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all())
#     reviewer = serializers.PrimaryKeyRelatedField(read_only=True)
#
#     class Meta:
#         model = Review
#         fields = ('id', 'title', 'summary', 'rating', 'created', 'reviewer_ip', 'company', 'reviewer')
#         read_only_fields = ('reviewer_ip',)
#
#
