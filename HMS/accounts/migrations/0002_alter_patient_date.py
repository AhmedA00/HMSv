# Generated by Django 4.0.3 on 2022-03-27 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date',
            field=models.TimeField(),
        ),
    ]