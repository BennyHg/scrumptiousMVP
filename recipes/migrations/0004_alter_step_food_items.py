# Generated by Django 4.0.3 on 2022-06-03 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_step_food_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='food_items',
            field=models.ManyToManyField(blank=True, to='recipes.fooditem'),
        ),
    ]
