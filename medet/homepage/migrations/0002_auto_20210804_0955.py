# Generated by Django 3.0.6 on 2021-08-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Searc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_name', models.CharField(max_length=1000)),
                ('reason', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Search',
        ),
    ]