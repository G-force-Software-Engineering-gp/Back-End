# Generated by Django 4.2.6 on 2023-10-16 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tascrum", "0004_board_members_workspace_members"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="memberboardrole",
            name="board",
        ),
        migrations.RemoveField(
            model_name="memberboardrole",
            name="member",
        ),
        migrations.DeleteModel(
            name="Board",
        ),
        migrations.DeleteModel(
            name="MemberBoardRole",
        ),
    ]
