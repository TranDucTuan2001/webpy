# Generated by Django 5.0 on 2024-04-09 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_product_detai'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='detai',
            new_name='detail',
        ),
    ]
