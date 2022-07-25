# Generated by Django 4.0.6 on 2022-07-24 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_place_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='address',
        ),
        migrations.AddField(
            model_name='place',
            name='address_line',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='address_line2',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='postcode',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='state_province',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='town_city',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]