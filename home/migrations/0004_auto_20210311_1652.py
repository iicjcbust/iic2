# Generated by Django 3.1.6 on 2021-03-11 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210306_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='organizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_no', models.IntegerField()),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='organizers/')),
            ],
        ),
        migrations.AlterField(
            model_name='events',
            name='googleFormLink',
            field=models.URLField(blank=True, null=True),
        ),
    ]
