# Generated by Django 3.1.1 on 2020-11-16 15:05

from django.db import migrations, models
import pg.models


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0002_pgowner_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pgowner',
            name='img',
            field=models.ImageField(upload_to=pg.models.user_directory_path),
        ),
    ]
