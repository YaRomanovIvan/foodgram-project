from django import forms
from .models import Recipe, Tag


tag = Tag.objects.all()

FAVORITE_COLORS_CHOICES = [
]
for i in tag:
    FAVORITE_COLORS_CHOICES.append((i.pk, i.name))

class RecipeForm(forms.ModelForm):
    tags = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )

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
