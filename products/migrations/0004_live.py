# Generated by Django 3.1.2 on 2021-01-21 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_menn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Live',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('live_header', models.CharField(default='', max_length=120)),
                ('live_content', models.TextField(blank=True, null=True)),
                ('live_content_2', models.TextField(blank=True, null=True)),
                ('live_content_3', models.TextField(blank=True, null=True)),
                ('live_content_4', models.TextField(blank=True, null=True)),
                ('live_content_5', models.TextField(blank=True, null=True)),
                ('live_content_6', models.TextField(blank=True, null=True)),
                ('live_content_7', models.TextField(blank=True, null=True)),
                ('pris', models.DecimalField(decimal_places=0, max_digits=8)),
            ],
        ),
    ]