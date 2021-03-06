# Generated by Django 3.2.12 on 2022-05-29 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
        ("TODO", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="userSet",
            field=models.ManyToManyField(to="users.User"),
        ),
        migrations.AlterField(
            model_name="todo",
            name="dateCreate",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="todo",
            name="dateUpdate",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
