# Generated by Django 3.2.6 on 2021-08-19 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_merge_0002_auto_20181101_2355_0009_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('drinks', 'drinks'), ('entrees', 'entrees'), ('appetizers', 'appetizers'), ('treats', 'treats')], max_length=60),
        ),
    ]
