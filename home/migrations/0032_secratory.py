# Generated by Django 3.1.6 on 2021-06-30 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_incubationstudents_innovationstudents_iprstudents_startupstudents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Secratory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
