# Generated by Django 5.1.3 on 2024-11-19 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edit', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]