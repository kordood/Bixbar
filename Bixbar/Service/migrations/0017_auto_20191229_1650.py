# Generated by Django 2.2.4 on 2019-12-29 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bixbar', '0016_auto_20191229_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipemodel',
            name='cocktail',
            field=models.ManyToManyField(to='bixbar.Cocktail'),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='recipe2',
            field=models.TextField(null=True),
        ),
    ]
