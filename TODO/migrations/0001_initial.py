# Generated by Django 3.2.12 on 2022-05-29 16:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nameProject", models.CharField(max_length=64)),
                ("linkProject", models.CharField(max_length=64)),
                ("userSet", models.ManyToManyField(to="users.User")),
            ],
        ),
        migrations.CreateModel(
            name="TODO",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("text", models.CharField(max_length=1024)),
                ("dateCreate", models.DateTimeField()),
                ("dateUpdate", models.DateTimeField()),
                ("project", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="TODO.project")),
                ("user", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="users.user")),
            ],
        ),
    ]