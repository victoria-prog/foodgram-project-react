# Generated by Django 3.0.5 on 2021-09-16 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210914_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoriterecipes',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fav_recipes', to='api.Recipe'),
        ),
    ]
