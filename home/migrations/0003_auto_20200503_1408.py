# Generated by Django 3.0.5 on 2020-05-03 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200503_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='reccomend',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='firstpage_rec',
        ),
    ]
