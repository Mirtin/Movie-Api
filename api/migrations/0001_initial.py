# Generated by Django 4.2.11 on 2024-04-28 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='api/images')),
                ('trailer', models.FileField(upload_to='api/trailers')),
            ],
        ),
    ]
