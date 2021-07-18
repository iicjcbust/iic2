# Generated by Django 3.1.6 on 2021-06-26 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20210626_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iprcoordinator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Iprmember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Incubationimage',
        ),
        migrations.DeleteModel(
            name='Innovationimage',
        ),
        migrations.DeleteModel(
            name='Iprimage',
        ),
        migrations.DeleteModel(
            name='Startupimage',
        ),
    ]
