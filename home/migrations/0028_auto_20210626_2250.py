# Generated by Django 3.1.6 on 2021-06-26 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_incubationcoordinator_incubationupmember_startupcoordinator_startupmember'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iicfaculty',
            old_name='title',
            new_name='name',
        ),
    ]