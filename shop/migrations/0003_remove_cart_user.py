# Generated by Django 4.1 on 2022-09-11 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_item_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="user",
        ),
    ]
