# Generated by Django 3.2.5 on 2021-07-28 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0048_alter_cordinator_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achivementsnew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.URLField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Achivements',
        ),
    ]
