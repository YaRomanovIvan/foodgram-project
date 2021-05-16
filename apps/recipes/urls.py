from unicodedata import name
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('recipe/<str:author>/<slug:slug>/', views.recipe_view, name='recipe_view'),
    path('create_recipe/', views.create_recipe, name='create_recipe')
]