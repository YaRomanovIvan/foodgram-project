from django import forms
from .models import Recipe, Tag


class RecipeForm(forms.ModelForm):
    tags = forms.CheckboxSelectMultiple()

    class Meta:
        model = Recipe
        fields = (
            "title",
            "tags",
            "ingredient",
            "time_cooking",
            "description",
            "image",
        )
