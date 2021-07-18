# Generated by Django 3.1.6 on 2021-07-04 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_homeslider'),
    ]

    operations = [
        migrations.CreateModel(
            name='cordinator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(blank=True, max_length=200, null=True)),
                ('role', models.CharField(choices=[('Ipr Co-ordinator', 'Ipr Co-ordinator'), ('Ipr Member', 'Ipr Member'), ('Innovation Co-ordinator', 'Innovation Co-ordinator'), ('Innovation Member', 'Innovation Member'), ('Startup Co-ordinator', 'Startup Co-ordinator'), ('Startup Member', 'Startup Member'), ('Incubation Co-ordinator', 'Incubation Co-ordinator'), ('Incubationup Member', 'Incubationup Member'), ('IIC Faculty', 'IIC Faculty'), ('Ipr Students', 'Ipr Students'), ('Innovation Students', 'Innovation Students'), ('Startup Students', 'Startup Students'), ('Incubation Students', 'Incubation Students'), ('Secratory', 'Secratory')], max_length=50)),
                ('createdDate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]