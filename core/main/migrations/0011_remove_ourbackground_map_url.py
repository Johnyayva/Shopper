# Generated by Django 4.2.1 on 2023-05-13 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_ourbackground'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ourbackground',
            name='map_url',
        ),
    ]
