from django.db.models import Q
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from shop.models import Recipe
from shop.serializers import RecipeSerializer


# Create your views here.
class search(APIView):
    def get(self,request):
        query=self.request.query_params.get('search')
        if (query):
                b=Recipe.objects.filter(Q(recipe_name__icontains=query)|Q(cuisine__icontains=query)|Q(mealtype__icontains=query)|Q(ingredients__icontains=query)|Q(desc__icontains=query))
                p=RecipeSerializer(b,many=True)
                return Response(p.data)