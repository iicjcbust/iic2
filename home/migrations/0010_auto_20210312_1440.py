# Generated by Django 3.1.6 on 2021-03-12 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='person_name',
        ),
    ]