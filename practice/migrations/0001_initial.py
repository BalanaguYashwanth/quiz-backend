# Generated by Django 3.1.1 on 2020-11-20 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number1', models.IntegerField()),
                ('number2', models.IntegerField()),
                ('result', models.IntegerField()),
            ],
        ),
    ]
