# Generated by Django 2.2.17 on 2020-12-06 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AduanaNacional', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=200, verbose_name='Apellido')),
            ],
        ),
    ]
