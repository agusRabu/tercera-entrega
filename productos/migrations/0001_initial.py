# Generated by Django 4.2.6 on 2023-11-02 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.TextField()),
                ('stock', models.TextField()),
                ('categoria', models.IntegerField()),
            ],
        ),
    ]
