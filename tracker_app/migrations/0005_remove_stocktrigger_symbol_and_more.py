# Generated by Django 4.0.5 on 2022-07-06 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0004_stocktrigger'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocktrigger',
            name='symbol',
        ),
        migrations.AddField(
            model_name='stocktrigger',
            name='stock_tracker',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tracker_app.stocktracker'),
        ),
    ]
