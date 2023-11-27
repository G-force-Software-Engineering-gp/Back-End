# Generated by Django 4.2.6 on 2023-11-27 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tascrum", "0031_card_description_alter_cardlabel_unique_together"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="survey",
            name="created_by",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="questions",
        ),
        migrations.RemoveField(
            model_name="burndownchart",
            name="user",
        ),
        migrations.AddField(
            model_name="burndownchart",
            name="board",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="burndown_charts",
                to="tascrum.board",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="burndownchart",
            name="member",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="burndown_charts",
                to="tascrum.member",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="burndownchart",
            name="done",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="burndownchart",
            name="estimate",
            field=models.FloatField(default=0),
        ),
        migrations.DeleteModel(
            name="Question",
        ),
        migrations.DeleteModel(
            name="Survey",
        ),
    ]
