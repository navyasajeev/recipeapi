"""recipeapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import SimpleRouter
from shop import views
from django.conf import settings
from rest_framework.authtoken import views as rviews
from django.conf.urls.static import static


from django.urls import path, include

#
# router = routers.DefaultRouter()
#
# # router.register("products", views.ProductViewSet)
#
# recipe_router = routers.NestedDefaultRouter(router, "recipe", lookup='recipe')
# recipe_router.register("ratings", views.RatingViewSet, basename="rating")


router=SimpleRouter()
router.register('recipe',views.RecipeDetails)
router.register('rating',views.AllRatingDetails)
router.register('user',views.CreateUser)
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('shop.urls')),
# path('review/',views.ReviewDetail.as_view(),name='search'),
   path('search/', include('search.urls')),
path('',include(router.urls)),
path('shop/',include('shop.urls')),
    # path("", include(recipe_router.urls)),

path('login/',rviews.obtain_auth_token),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

