# Generated by Django 4.1.5 on 2023-01-29 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='img_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
