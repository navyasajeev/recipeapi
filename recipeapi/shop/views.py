from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Recipe
from shop.serializers import RecipeSerializer
from shop.serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from shop.models import Rating
from shop.serializers import RatingSerializer


# Create your views here.




class RecipeDetails(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset=Recipe.objects.all()

    serializer_class=RecipeSerializer






class CreateUser(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer






# class RatingDetails(viewsets.ModelViewSet):
#     # permission_classes = [IsAuthenticated]
#     queryset = Rating.objects.all()
#     serializer_class = RatingSerializer
#
#
#     def get_queryset(self,request,pk):
#         qs=self.queryset
#         queryset=qs.filter(recipe=pk)
#         return queryset


class RatingDetails(APIView):
    def get_objects(self,request,pk):
        try:
            return Recipe.objects.get(pk=pk)
        except:
            raise Http404
    def get(self,request,pk):
            c=self.get_objects(request,pk)
            p=Rating.objects.filter(recipe=c)
            rec=RatingSerializer(p,many=True)
            return Response(rec.data)

class AddRating(APIView):
    def get_objects(self,request,pk):
        try:
            return Recipe.objects.get(pk=pk)
        except:
            raise Http404
    def post(self,request,pk):
        st=self.get_objects(request,pk)
        s=RatingSerializer(st,data=request.data)
        if s.is_valid():
            a=s.validated_data['rating']
            p=s.validated_data['review']

            o=Rating.objects.create(rating=a,review=p)
            o.save()

            return Response(s.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)



class AllRatingDetails(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer