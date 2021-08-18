# Generated by Django 3.2.6 on 2021-08-17 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('entrees', 'entrees'), ('drinks', 'drinks'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]
