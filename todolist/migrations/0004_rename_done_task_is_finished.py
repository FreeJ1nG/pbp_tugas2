# Generated by Django 4.1 on 2022-09-27 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todolist", "0003_task_done"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="done",
            new_name="is_finished",
        ),
    ]
