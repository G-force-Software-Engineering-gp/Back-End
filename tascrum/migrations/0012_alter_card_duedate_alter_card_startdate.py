# Generated by Django 4.2.6 on 2023-10-27 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tascrum', '0011_card_duedate_card_startdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='duedate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='startdate',
            field=models.DateTimeField(null=True),
        ),
    ]
