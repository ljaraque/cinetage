# Generated by Django 3.1.6 on 2021-03-02 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pelicula',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='temporal_idioma',
            field=models.IntegerField(null=True),
        ),
    ]
