# Generated by Django 2.1.15 on 2021-02-02 21:39

import appcore.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcore', '0004_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=appcore.models.recipe_image_file_path),
        ),
    ]
