# Generated by Django 4.1 on 2022-09-26 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todolist", "0002_alter_task_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="done",
            field=models.BooleanField(default=False),
        ),
    ]
