# Generated by Django 4.1 on 2022-10-27 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
    ]