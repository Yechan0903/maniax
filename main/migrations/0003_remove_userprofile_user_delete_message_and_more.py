# Generated by Django 5.0.7 on 2024-07-30 19:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_message_userprofile"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="user",
        ),
        migrations.DeleteModel(
            name="Message",
        ),
        migrations.DeleteModel(
            name="UserProfile",
        ),
    ]