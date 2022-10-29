# Generated by Django 4.1.2 on 2022-10-29 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Наименование товара')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Оисание товара')),
                ('category', models.CharField(choices=[('other', 'Разное'), ('notebook', 'Ноутбуки'), ('smartphone', 'Смартфоны')], default='other', max_length=30, verbose_name='Категория')),
                ('image', models.ImageField(blank=True, default='plug/nophoto.png', null=True, upload_to='images', verbose_name='Фото товара')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=2000, verbose_name='Текст комментария')),
                ('rating', models.IntegerField(verbose_name='Оценка')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reviews', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_reviews', to='shop.product', verbose_name='Товар')),
            ],
        ),
    ]