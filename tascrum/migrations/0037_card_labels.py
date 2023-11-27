# Generated by Django 4.2.6 on 2023-11-27 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tascrum', '0036_remove_card_labels'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='labels',
            field=models.ManyToManyField(related_name='clabel', through='tascrum.CardLabel', to='tascrum.lable'),
        ),
    ]
