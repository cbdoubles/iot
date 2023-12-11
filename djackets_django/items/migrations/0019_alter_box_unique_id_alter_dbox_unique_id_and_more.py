# Generated by Django 4.2.7 on 2023-12-11 10:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0018_alter_box_unique_id_alter_dbox_unique_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('b01dc067-f6be-4f14-b082-2bff6c2b4e15'), max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='dbox',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('262490be-e46d-4f87-9d1d-85a879b41c50'), max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('be699baf-6ced-4598-9ddf-c2e4df3b5a4f'), max_length=100, null=True, unique=True),
        ),
    ]
