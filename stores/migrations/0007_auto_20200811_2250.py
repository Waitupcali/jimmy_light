# Generated by Django 2.2.5 on 2020-08-11 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0006_auto_20200811_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stores', to='stores.Store'),
        ),
        migrations.AlterField(
            model_name='store',
            name='facilities',
            field=models.ManyToManyField(blank=True, related_name='stores', to='stores.Facility'),
        ),
    ]