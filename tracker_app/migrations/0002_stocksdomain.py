# Generated by Django 4.0.5 on 2022-07-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StocksDomain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('company_name', models.CharField(max_length=50)),
            ],
        ),
    ]
