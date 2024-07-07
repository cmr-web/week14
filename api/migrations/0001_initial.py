# Generated by Django 5.0.6 on 2024-07-07 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('rollno', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('occupation', models.CharField(max_length=20)),
                ('profile', models.CharField(max_length=2000)),
            ],
        ),
    ]
