# Generated by Django 4.0.5 on 2022-07-06 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0006_alter_stocktrigger_stock_tracker'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stocktrigger',
            old_name='stock_tracker',
            new_name='stock',
        ),
    ]