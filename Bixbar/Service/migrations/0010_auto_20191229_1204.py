# Generated by Django 2.2.4 on 2019-12-29 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bixbar', '0009_auto_20191229_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='Profile',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
