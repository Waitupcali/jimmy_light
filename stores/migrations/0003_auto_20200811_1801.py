# Generated by Django 2.2.5 on 2020-08-11 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_auto_20200811_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='store',
            name='store_type',
        ),
        migrations.AddField(
            model_name='store',
            name='store_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stores.StoreType'),
        ),
        migrations.AddField(
            model_name='store',
            name='facilities',
            field=models.ManyToManyField(blank=True, related_name='rooms', to='stores.Facility'),
        ),
    ]
