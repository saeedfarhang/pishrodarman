# Generated by Django 3.0.5 on 2020-05-30 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200531_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
