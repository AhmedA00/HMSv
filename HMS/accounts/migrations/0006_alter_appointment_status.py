# Generated by Django 4.0.3 on 2022-03-28 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_appointment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('Booked', 'Booked'), ('Available', 'Available'), ('Waiting', 'Waiting')], max_length=200, null=True),
        ),
    ]
