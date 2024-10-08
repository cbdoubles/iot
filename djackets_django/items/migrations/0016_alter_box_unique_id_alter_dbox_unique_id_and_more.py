# Generated by Django 4.2.7 on 2023-12-11 10:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0015_alter_box_unique_id_alter_dbox_unique_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('33c7bf79-0832-4c61-9d67-14b511038ac2'), max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='dbox',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('3e98ef1f-7568-4c5c-ac8c-1da39c937f37'), max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('14fb3417-72ed-480e-940a-7b82c0a00810'), max_length=100, null=True, unique=True),
        ),
    ]
