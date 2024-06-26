# Generated by Django 5.0.2 on 2024-02-23 19:28

import django.core.validators
import django.db.models.deletion
import exam_prep_ll.fruits.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'This fruit name is already in use! Try a new one.'}, max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(2), exam_prep_ll.fruits.models.validate_only_letters])),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('nutrition', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='profiles.profile')),
            ],
        ),
    ]
