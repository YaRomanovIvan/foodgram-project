from django.urls import path
from . import views

urlpatterns = [
    path('v1/ingredients/', views.IngredientApi.as_view())
]