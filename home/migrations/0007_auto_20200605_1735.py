# Generated by Django 3.0.5 on 2020-06-05 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_product_preference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='preference',
            field=models.CharField(blank=True, choices=[('1', 'first'), ('2', 'secend'), ('3', 'third')], max_length=128, null=True),
        ),
    ]
