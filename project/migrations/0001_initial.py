<<<<<<< HEAD
# Generated by Django 3.1.7 on 2021-02-27 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=100)),
                ('memo', models.TextField()),
            ],
        ),
    ]
=======
# Generated by Django 3.1.6 on 2021-02-27 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('memo', models.TextField()),
            ],
        ),
    ]
>>>>>>> 7baf0dce4a0ea4a33394292b51bb8f4256b01695