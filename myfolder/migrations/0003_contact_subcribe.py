# Generated by Django 5.0.2 on 2024-03-13 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfolder', '0002_job_type2_team_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=60)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subcribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gmail', models.CharField(max_length=100)),
            ],
        ),
    ]
