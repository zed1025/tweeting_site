# Generated by Django 3.1.1 on 2020-09-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_auto_20200910_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='body',
            field=models.TextField(max_length=255),
        ),
    ]