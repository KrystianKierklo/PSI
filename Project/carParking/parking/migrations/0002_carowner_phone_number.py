# Generated by Django 4.1.2 on 2022-11-26 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carowner',
            name='phone_number',
            field=models.CharField(default=123456789, max_length=9),
            preserve_default=False,
        ),
    ]
