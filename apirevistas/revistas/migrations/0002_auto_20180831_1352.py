# Generated by Django 2.1 on 2018-08-31 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revistas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revista',
            name='codigo',
            field=models.IntegerField(unique=True),
        ),
    ]
