# Generated by Django 3.1.6 on 2021-06-26 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_delete_homeslider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Downloadtable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=300)),
            ],
        ),
    ]
