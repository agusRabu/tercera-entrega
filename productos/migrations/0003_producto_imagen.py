# Generated by Django 4.2.6 on 2023-12-15 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_alter_producto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='default.jpg', null=True, upload_to='confirmar'),
        ),
    ]