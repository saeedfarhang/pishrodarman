# Generated by Django 3.0.5 on 2020-06-05 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products_category',
            name='slug',
            field=models.SlugField(default='test'),
        ),
    ]
