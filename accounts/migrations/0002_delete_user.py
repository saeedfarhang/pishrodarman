# Generated by Django 3.0.5 on 2020-05-24 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
    ]