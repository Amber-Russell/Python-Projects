# Generated by Django 3.2.6 on 2021-08-18 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('treats', 'treats'), ('entrees', 'entrees'), ('drinks', 'drinks')], max_length=60),
        ),
    ]
