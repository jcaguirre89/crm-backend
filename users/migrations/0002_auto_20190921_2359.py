# Generated by Django 2.2.5 on 2019-09-21 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_contractor',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_vendor',
        ),
    ]