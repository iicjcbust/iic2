# Generated by Django 3.1.6 on 2021-03-11 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210311_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='Eventorganizer1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.organizer'),
        ),
    ]
