# Generated by Django 3.1.2 on 2020-11-06 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendemail', '0003_auto_20201106_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(default=''),
        ),
    ]
