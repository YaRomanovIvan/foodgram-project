from apps.recipes.models import Recipe, RecipeIngredient, Tag, User, Follow
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required

def index(request):
    recipes = Recipe.objects.all()
    tags = Tag.objects.all()
    context = {
        "recipes": recipes,
        "tags": tags,
    }
    return render(request, "foodgram/index.html", context)


def recipe_view(request, author, slug):
    recipe = get_object_or_404(Recipe, slug=slug, author__username=author)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe.pk)
    context = {
        "recipe": recipe,
        "ingredients": ingredients,
    }
    return render(request, "foodgram/recipe_view.html", context)


def create_recipe(request):
    if request.method != "POST":
        return render(
            request, "foodgram/create_recipe.html", {"form": RecipeForm()}
        )
    form = RecipeForm(request.POST, files=request.FILES or None)
    if not form.is_valid():
        form = RecipeForm(request.POST, files=request.FILES or None)
        return render(request, "foodgram/create_recipe.html", {"form": form})
    user = form.save(commit=False)
    user.author = request.user
    user.save()
    return redirect("index")


def author_recipe(request, author):
    author_recipe = get_object_or_404(User, username=author)
    tags = Tag.objects.all()
    recipes = author_recipe.author.all()
    context = {
        'author': author_recipe,
        'recipes': recipes,
        'tags': tags,
    }
    return render(request, 'foodgram/authorRecipe.html', context)


@login_required
def profile_follow(request, username):
    author = get_object_or_404(User, username=username)
    user = get_object_or_404(User, username=request.user)
    if author == user:
        return redirect("index")

    if author.following.filter(user=request.user.id).exists():
        return redirect("index")
    follow = Follow.objects.create(author=author, user=user)
    follow.save()
    return redirect("profile", author)