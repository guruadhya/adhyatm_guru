# Generated by Django 3.2.23 on 2023-11-19 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prakalp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('main_image', models.ImageField(upload_to='prakalp_images')),
            ],
        ),
        migrations.CreateModel(
            name='PrakalpImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='prakalp_images')),
                ('prakalp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prakalp.prakalp')),
            ],
            options={
                'db_table': 'prakalp_image',
            },
        ),
    ]
