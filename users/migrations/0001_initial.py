# Generated by Django 5.0.6 on 2024-06-06 13:14

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
            name='Userss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=20, verbose_name='Soyad')),
                ('addresstolive', models.CharField(max_length=20, verbose_name='Yaşadığı ünvan')),
                ('address', models.CharField(max_length=20, verbose_name='Ünvan')),
                ('specialty', models.TextField(max_length=50, verbose_name='Ixtisas')),
                ('age', models.CharField(max_length=20, verbose_name='Yaşı')),
                ('hobbies', models.TextField(max_length=50, verbose_name='Hobiləri')),
                ('university', models.TextField(max_length=50, verbose_name='Universitet')),
                ('name', models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ad')),
            ],
        ),
    ]