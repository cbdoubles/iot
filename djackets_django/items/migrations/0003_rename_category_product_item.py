# Generated by Django 4.2.7 on 2023-11-30 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_remove_item_description_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='item',
        ),
    ]
