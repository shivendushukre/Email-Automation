# Generated by Django 3.0.8 on 2022-01-06 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
