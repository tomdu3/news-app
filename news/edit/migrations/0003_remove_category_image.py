# Generated by Django 5.1.3 on 2024-11-17 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("edit", "0002_alter_category_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="image",
        ),
    ]