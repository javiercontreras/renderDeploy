# Generated by Django 5.1.2 on 2024-10-28 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='precio',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]