# Generated by Django 4.2.6 on 2023-12-14 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tascrum', '0034_alter_meeting_options_meeting_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatbot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_message', models.CharField(max_length=500)),
            ],
        ),
    ]
