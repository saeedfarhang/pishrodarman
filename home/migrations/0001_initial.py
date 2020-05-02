# Generated by Django 3.0.5 on 2020-05-02 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persian_name', models.CharField(max_length=150)),
                ('english_name', models.CharField(max_length=150)),
                ('ditail', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.products_category')),
            ],
        ),
    ]
