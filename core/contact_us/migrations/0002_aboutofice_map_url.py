# Generated by Django 4.2.1 on 2023-05-12 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutofice',
            name='map_url',
            field=models.URLField(default='', verbose_name='Map Url'),
        ),
    ]
