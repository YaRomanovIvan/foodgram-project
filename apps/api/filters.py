from django_filters import rest_framework as django_filters
from apps.recipes.models import Ingredient


class IngredientFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name="title",
        lookup_expr="icontains",
    )

    class Meta:
        model = Ingredient
        fields = [
            "title",
        ]