# Generated by Django 3.0.6 on 2020-06-01 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='password',
            field=models.CharField(default='', max_length=300),
        ),
    ]
