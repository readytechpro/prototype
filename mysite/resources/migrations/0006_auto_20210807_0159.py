# Generated by Django 3.1.6 on 2021-08-07 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_auto_20210807_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learningresource',
            name='tags',
            field=models.ManyToManyField(to='resources.CategoryTag'),
        ),
    ]