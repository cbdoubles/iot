# Generated by Django 4.2.7 on 2024-01-08 10:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0027_remove_product_box_uid_alter_box_unique_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='unique_ID',
        ),
        migrations.AlterField(
            model_name='box',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('86ff6cf9-c8de-4cf9-ab21-062b37e63e7f'), max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='dbox',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('a6449d3e-c1cf-4e1d-a42c-1fee58e1fd37'), max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.TextField(help_text='Required', verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nfc_number',
            field=models.CharField(blank=True, default=uuid.UUID('147858f9-97f5-491f-adc0-d83bcbe0e160'), max_length=100, null=True, unique=True),
        ),
    ]
