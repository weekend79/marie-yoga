# Generated by Django 3.1.2 on 2020-11-23 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='about_content_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='about_content_3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='about_content_4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='about_content_5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='about_content_6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='header_text_2',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_header',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='about',
            name='header_text',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
    ]
