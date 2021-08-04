# Generated by Django 3.1.6 on 2021-08-04 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteering', '0002_auto_20210312_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='volunteerproject',
            name='tagline',
            field=models.CharField(default='No Tag Line', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='volunteerproject',
            name='tags',
            field=models.ManyToManyField(to='volunteering.CategoryTag'),
        ),
    ]