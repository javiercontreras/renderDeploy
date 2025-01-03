# Generated by Django 5.1.2 on 2024-10-24 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flan_uuid', models.UUIDField()),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('img_url', models.TextField()),
                ('slug', models.SlugField()),
                ('is_private', models.BooleanField()),
            ],
        ),
    ]
