# Generated by Django 4.2.17 on 2025-01-03 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_club_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='current_book',
        ),
    ]
