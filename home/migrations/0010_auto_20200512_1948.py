# Generated by Django 3.0.5 on 2020-05-12 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200512_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(default='media.tabsanj.png', max_length=300, upload_to=''),
        ),
    ]