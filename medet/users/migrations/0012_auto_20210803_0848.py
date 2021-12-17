# Generated by Django 3.0.6 on 2021-08-03 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20210803_0559'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='disease',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='doctor_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='schedule',
            field=models.TextField(null=True),
        ),
    ]