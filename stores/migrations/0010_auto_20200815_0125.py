# Generated by Django 2.2.5 on 2020-08-14 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0009_auto_20200811_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='luggage_large_store',
            field=models.IntegerField(default=3, help_text='size: confirmed later'),
        ),
        migrations.AlterField(
            model_name='store',
            name='luggage_medium_store',
            field=models.IntegerField(default=3, help_text='size: confirmed later'),
        ),
        migrations.AlterField(
            model_name='store',
            name='luggage_small_store',
            field=models.IntegerField(default=3, help_text='size: confirmed later'),
        ),
    ]
