# Generated by Django 5.0 on 2024-01-01 00:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('biography', models.TextField(blank=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField(blank=True)),
                ('contact_email', models.EmailField(blank=True, max_length=254)),
                ('contact_phone', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('publication_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cover_image', models.URLField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryApp.author')),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='libraryApp.genre')),
                ('publisher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='libraryApp.publisher')),
            ],
        ),
        migrations.CreateModel(
            name='BookCopy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copy_number', models.CharField(max_length=50)),
                ('condition', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('is_available', models.BooleanField(default=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryApp.book')),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('book_copy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryApp.bookcopy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('bio', models.TextField(blank=True)),
                ('email', models.EmailField(default='default@example.com', max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
