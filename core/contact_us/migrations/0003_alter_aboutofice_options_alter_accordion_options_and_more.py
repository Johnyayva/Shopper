# Generated by Django 4.2.1 on 2023-05-13 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0002_aboutofice_map_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutofice',
            options={'verbose_name': 'SAbout Ofice', 'verbose_name_plural': 'About Ofice'},
        ),
        migrations.AlterModelOptions(
            name='accordion',
            options={'verbose_name': 'Accordion', 'verbose_name_plural': 'Accordions'},
        ),
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name': 'Contact Us', 'verbose_name_plural': 'Contact Us'},
        ),
    ]
