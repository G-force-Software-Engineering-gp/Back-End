# Generated by Django 4.2.6 on 2023-11-15 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tascrum", "0025_board_lastseen_alter_board_backgroundimage"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="card",
            options={"ordering": ("order",)},
        ),
        migrations.AddField(
            model_name="card",
            name="order",
            field=models.IntegerField(null=True),
        ),
    ]
