# Generated by Django 3.2.7 on 2021-11-04 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0008_timetable'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='day',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
