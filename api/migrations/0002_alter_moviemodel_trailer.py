# Generated by Django 4.2.11 on 2024-04-28 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviemodel',
            name='trailer',
            field=models.FileField(default='', upload_to='api/trailers'),
        ),
    ]
