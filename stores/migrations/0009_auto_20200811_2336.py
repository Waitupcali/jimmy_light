# Generated by Django 2.2.5 on 2020-08-11 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0008_auto_20200811_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='store_photos'),
        ),
    ]