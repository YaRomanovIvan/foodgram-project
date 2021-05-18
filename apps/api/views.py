from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework.utils import json
from apps.recipes.models import Ingredient, RecipeIngredient, Recipe


class IngredientApi(LoginRequiredMixin, View):
    def get(self, request):
        text = request.GET['query']
        ingredients = list(Ingredient.objects.filter(
            title__icontains=text).values('title', 'unit'))
        return JsonResponse(ingredients, safe=False)