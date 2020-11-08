# Generated by Django 3.1.2 on 2020-11-06 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_course_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=125)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('course_name', models.CharField(max_length=125)),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=1)),
                ('course_date', models.DateField()),
                ('course_time', models.TimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=8),
        ),
    ]
