# Generated by Django 2.2.4 on 2019-12-29 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bixbar', '0017_auto_20191229_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipemodel',
            old_name='cocktail',
            new_name='cocktail2',
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='cocktail2',
            field=models.ManyToManyField(to='bixbar.Cocktail'),
        ),
    ]
