# Generated by Django 4.2.6 on 2023-10-30 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tascrum', '0015_board_backgroundimage_alter_membercardrole_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberboardrole',
            name='role',
            field=models.CharField(default='member', max_length=50),
        ),
    ]
