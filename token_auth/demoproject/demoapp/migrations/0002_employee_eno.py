# Generated by Django 3.2 on 2021-06-14 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='eno',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
