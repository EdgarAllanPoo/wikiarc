# Generated by Django 3.1.7 on 2021-04-01 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='Ini Judul')),
                ('body', models.TextField(default='Ini Isi')),
            ],
        ),
    ]
