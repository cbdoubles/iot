# Generated by Django 4.2.7 on 2023-12-11 10:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0014_alter_box_unique_id_alter_dbox_unique_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('0f4978f4-8f93-412e-9b56-b168e59fc28b'), max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='dbox',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('7afb426b-757b-4f10-a278-f6e4e6d06930'), max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('87d0063a-346f-4543-966e-4706caf5f9a3'), max_length=100, null=True, unique=True),
        ),
    ]
