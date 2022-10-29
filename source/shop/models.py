from django.db import models
from django.db.models import TextChoices
from django.contrib.auth import get_user_model

class CategoryChoices(TextChoices):
    OTHER = 'other', 'Разное'
    NOUTBOOK = 'notebook', 'Ноутбуки'
    SMARTPHONE = 'smartphone', 'Смартфоны'


class Product(models.Model):
    title = models.CharField(
        verbose_name = 'Наименование товара',
        max_length = 100,
        null = False,
        blank = False
    )
    description = models.TextField(
        verbose_name = 'Оисание товара',
        max_length = 2000,
        null = True,
        blank = True
    )
    category = models.CharField(
        verbose_name = 'Категория',
        max_length = 30,
        choices = CategoryChoices.choices,
        null = False,
        blank = False,
        default = CategoryChoices.OTHER
    )
    image = models.ImageField(
        verbose_name='Фото товара',
        null=True,
        blank=True,
        upload_to='images',
        default='plug/nophoto.png'
    )

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='user_reviews',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        verbose_name='Товар',
        to='shop.Product',
        related_name='product_reviews',
        on_delete=models.CASCADE
    )
    text = models.TextField(
        verbose_name='Текст комментария',
        max_length = 2000,
        null = False,
        blank = False
    )
    rating = models.IntegerField(
        verbose_name = 'Оценка',
        null = False,
        blank = False
    )

