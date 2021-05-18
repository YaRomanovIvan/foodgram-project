from apps.recipes.models import Recipe, RecipeIngredient, Tag, User, Follow, Ingredient, RecipeTag
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RecipeForm
from .utils import get_ingredients
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
    user = get_object_or_404(User, username=request.user)
    tags = Tag.objects.all()
    if request.method != "POST":
        return render(
            request, "foodgram/create_recipe.html", {"form": RecipeForm(), 'tags':tags}
        )
    form = RecipeForm(request.POST, files=request.FILES or None)
    ingr = get_ingredients(request)
    checkbox_tag = request.POST.getlist('checkbox')
    print(ingr)
    if not form.is_valid():
        form = RecipeForm(request.POST, files=request.FILES or None)
        return render(request, "foodgram/create_recipe.html", {"form": form})
    recipe = form.save(commit=False)
    recipe.author = user
    recipe.save()
    for pk in checkbox_tag:
        tag = get_object_or_404(Tag, pk=pk)
        recipetag = RecipeTag(
            recipe=recipe,
            tags=tag
        )
        recipetag.save()
    for ingr_name, amount in ingr.items():
        ingr_obj = get_object_or_404(Ingredient, title=ingr_name)
        ingr_recipe = RecipeIngredient(
            ingredient=ingr_obj,
            recipe=recipe,
            amount=amount,
        )
        ingr_recipe.save()
    form.save_m2m()
    return redirect('index')


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