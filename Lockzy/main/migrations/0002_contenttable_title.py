# Generated by Django 3.0.8 on 2020-07-30 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenttable',
            name='title',
            field=models.CharField(default='TITLE', max_length=128),
        ),
    ]