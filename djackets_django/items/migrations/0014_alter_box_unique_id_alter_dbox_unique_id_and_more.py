# Generated by Django 4.2.7 on 2023-12-11 10:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0013_product_unique_id_alter_box_unique_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('b133e5cd-9520-473f-9009-77509456a912'), max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='dbox',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('a128c94d-f49d-4917-812c-9782eb7a4675'), max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('defa6d34-09e2-4215-95fa-1db651fc403c'), max_length=100, null=True, unique=True),
        ),
    ]
