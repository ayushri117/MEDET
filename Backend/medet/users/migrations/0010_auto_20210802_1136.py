# Generated by Django 3.0.6 on 2021-08-02 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210802_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
    ]