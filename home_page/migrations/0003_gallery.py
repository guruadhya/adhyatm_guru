# Generated by Django 3.2.23 on 2023-11-20 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0002_livetv_socialmediaicons'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery_images')),
            ],
            options={
                'db_table': 'gallery_images',
            },
        ),
    ]
