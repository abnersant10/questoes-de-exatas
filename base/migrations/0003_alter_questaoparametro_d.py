# Generated by Django 4.1 on 2022-08-11 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_questaoparametro_d_alter_questaoparametro_a_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questaoparametro',
            name='D',
            field=models.FloatField(default=1),
        ),
    ]
