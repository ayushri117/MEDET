# Generated by Django 3.0.6 on 2021-08-03 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20210803_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='image',
            field=models.ImageField(blank=True, default='default_med_image.jpg', upload_to='medicine_pics'),
        ),
    ]