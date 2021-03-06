# Generated by Django 2.0.3 on 2018-03-28 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiRemoteCommand',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='MiRemoteDevice',
            fields=[
                ('dev_ID', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('ip', models.CharField(max_length=15, unique=True)),
                ('token', models.CharField(max_length=200)),
            ],
        ),
    ]
