# Generated by Django 3.0.5 on 2020-05-25 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200525_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='location',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]