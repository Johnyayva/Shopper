# Generated by Django 4.2.1 on 2023-05-12 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutOfice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('text_1', models.TextField(verbose_name='Text 1')),
                ('text_2', models.TextField(verbose_name='Text 2')),
                ('facebook_url', models.URLField(blank=True, verbose_name='Facebook Url')),
                ('twitter_url', models.URLField(blank=True, verbose_name='Twitter Url')),
                ('linked_in_url', models.URLField(blank=True, verbose_name='Linked in Url')),
                ('be_url', models.URLField(blank=True, verbose_name='Be Url')),
            ],
        ),
        migrations.CreateModel(
            name='Accordion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=254, verbose_name='User Email')),
                ('subject', models.CharField(max_length=250, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
            ],
        ),
    ]
