# Generated by Django 3.1.7 on 2021-02-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account_info',
            name='other_ID',
        ),
        migrations.RemoveField(
            model_name='account_info',
            name='slack_ID',
        ),
        migrations.RemoveField(
            model_name='account_info',
            name='univercity',
        ),
        migrations.AlterField(
            model_name='account_info',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
    ]