from operator import mod
from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Ingredient(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название",
    )
    unit = models.CharField(
        max_length=50,
        verbose_name="Еденица измерения",
    )

    class Meta:
        verbose_name_plural = "Ингредиенты"
        verbose_name = "Ингредиет"
        ordering = ["title"]

    def __str__(self):
        return f"{self.title}, {self.unit}"


class Tag(models.Model):
    name = models.CharField(
        max_length=25,
        verbose_name="Название",
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Слаг",
    )
    color = models.CharField(
        max_length=15,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = "Теги"
        verbose_name = "Тег"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name="Название рецепта",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="author",
        verbose_name="Автор",
    )
    image = models.ImageField(
        verbose_name="Картинка",
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    ingredient = models.ManyToManyField(
        Ingredient,
        through="RecipeIngredient",
        related_name="ingredient",
        verbose_name="Используемые ингредиеты",
    )
    tags = models.ManyToManyField(
        Tag,
        through="RecipeTag",
        related_name="tags",
        verbose_name="Теги",
    )
    time_cooking = models.PositiveIntegerField(
        verbose_name="Время приготовления",
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Слаг",
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name="Дата публикации"
    )

    class Meta:
        ordering = ["-pub_date"]
        verbose_name_plural = "Рецепты"
        verbose_name = "Рецепт"

    def __str__(self):
        return self.title


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorites",
        verbose_name="Пользователь",
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="favorites",
        verbose_name="Рецепт",
    )

    def __str__(self):
        return f"Избранный {self.recipe} у {self.user}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("user", "recipe"), name="unique_favorite_user_recipe"
            )
        ]

    verbose_name_plural = "Объекты избранного"
    verbose_name = "Объект избранного"


class RecipeTag(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
    )
    tags = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
    )


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
    )
    amount = models.PositiveIntegerField(
        verbose_name="Количество",
    )


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower",
        verbose_name="Пользователь",
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following", verbose_name="Автор"
    )

    class Meta:
        verbose_name = "Система подписки"

    def __str__(self):
        return f"Автор: {self.author}, Пользователь: {self.user}"
