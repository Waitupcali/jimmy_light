# Generated by Django 2.2.5 on 2020-08-11 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0007_auto_20200811_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='stores.Store'),
        ),
    ]
