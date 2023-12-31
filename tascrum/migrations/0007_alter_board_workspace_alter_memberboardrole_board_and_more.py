# Generated by Django 4.2.6 on 2023-10-16 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tascrum", "0006_board_memberboardrole_board_members_board_workspace"),
    ]

    operations = [
        migrations.AlterField(
            model_name="board",
            name="workspace",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="wboard",
                to="tascrum.workspace",
            ),
        ),
        migrations.AlterField(
            model_name="memberboardrole",
            name="board",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="brole",
                to="tascrum.board",
            ),
        ),
        migrations.AlterField(
            model_name="memberboardrole",
            name="member",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bmember",
                to="tascrum.member",
            ),
        ),
        migrations.AlterField(
            model_name="memberworkspacerole",
            name="member",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="mrole",
                to="tascrum.member",
            ),
        ),
        migrations.AlterField(
            model_name="memberworkspacerole",
            name="workspace",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="wrole",
                to="tascrum.workspace",
            ),
        ),
    ]
