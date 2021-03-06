# Generated by Django 3.1.6 on 2021-06-04 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_joiniic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annou',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileUpload', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('title', models.CharField(max_length=200)),
                ('EventLink', models.URLField(blank=True, null=True)),
                ('undertitle', models.CharField(max_length=200)),
                ('body', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='events',
            name='cell',
            field=models.CharField(choices=[('Institution’s Innovation Council (IICs)', 'Institution’s Innovation Council (IICs)'), ('Incubation Cell', 'Incubation Cell'), ('Innovation Cell', 'Innovation Cell'), ('Startup Cell', 'Startup Cell'), ('IPR Cell', 'IPR Cell')], max_length=50),
        ),
    ]
