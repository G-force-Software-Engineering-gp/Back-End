# Generated by Django 4.2.6 on 2023-10-15 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tascrum", "0003_workspace"),
    ]

    operations = [
        migrations.CreateModel(
            name="MemberWorkspace",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("Owner", "Owner"),
                            ("Admin", "Admin"),
                            ("Member", "Member"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tascrum.member"
                    ),
                ),
                (
                    "workspace",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tascrum.workspace",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="workspace",
            name="members",
            field=models.ManyToManyField(
                related_name="wmembers",
                through="tascrum.MemberWorkspace",
                to="tascrum.member",
            ),
        ),
    ]
