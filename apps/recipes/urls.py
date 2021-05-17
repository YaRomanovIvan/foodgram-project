from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path(
        "recipe/<str:author>/<slug:slug>/",
        views.recipe_view,
        name="recipe_view",
    ),
    path("create_recipe/", views.create_recipe, name="create_recipe"),
    path('recipe/<str:author>/', views.author_recipe, name='author_recipe'),
    path('follow/', views.profile_follow, name='follow'),
]
