# Generated by Django 2.2.5 on 2020-08-11 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_auto_20200811_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='store_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stores', to='stores.StoreType'),
        ),
    ]
