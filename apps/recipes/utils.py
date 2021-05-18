from django.http import request


def get_ingredients(request):
    ingredients = {}
    for key in dict(request.POST.items()):
        if 'nameIngredient' in key:
            a = key.split('_')
            ingredients[dict(request.POST.items())[key]] = int(request.POST[
                f'valueIngredient_{a[1]}'])

    return ingredients
