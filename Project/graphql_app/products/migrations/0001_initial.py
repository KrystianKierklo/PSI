# Generated by Django 4.1.3 on 2023-01-20 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registrynumber', models.CharField(max_length=10)),
                ('vehicalbrand', models.CharField(max_length=50)),
                ('vehicalmodel', models.CharField(max_length=50)),
                ('productionyear', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Parkingplaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placenumber', models.IntegerField()),
                ('dateofpurchase', models.DateTimeField()),
                ('car_registrynumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.car')),
            ],
        ),
        migrations.CreateModel(
            name='Carowner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=9)),
                ('name', models.CharField(max_length=45)),
                ('lastname', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('adress', models.CharField(max_length=120)),
                ('carregistrynumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.car')),
            ],
        ),
    ]
