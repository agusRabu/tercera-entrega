# Generated by Django 4.2.6 on 2023-12-15 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, default='/media/productos/default.jpg', null=True, upload_to='productos'),
        ),
    ]
