# Generated by Django 4.2.6 on 2023-10-15 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tascrum", "0005_alter_memberworkspacerole_member_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workspace",
            name="members",
            field=models.ManyToManyField(related_name="wmembers", to="tascrum.member"),
        ),
    ]
