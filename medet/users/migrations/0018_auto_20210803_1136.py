# Generated by Django 3.0.6 on 2021-08-03 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20210803_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='user',
        ),
        migrations.AlterField(
            model_name='medicine',
            name='disease_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='doctor_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Disease',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]
