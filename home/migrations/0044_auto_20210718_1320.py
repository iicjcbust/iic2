# Generated by Django 3.1.6 on 2021-07-18 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0043_auto_20210718_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='achivements',
            name='createdDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='downloadtable',
            name='createdDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='homeslider',
            name='createdDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]