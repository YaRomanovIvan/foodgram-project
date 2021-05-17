from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, Tag, RecipeTag


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1
    raw_id_fields = ("ingredient",)


class RecipeTagInline(admin.TabularInline):
    model = RecipeTag
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        RecipeIngredientInline,
        RecipeTagInline,
    ]
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("title", "unit")


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient)
