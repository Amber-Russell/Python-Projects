# Generated by Django 3.2.6 on 2021-08-19 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0007_alter_profiles_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='title',
            field=models.CharField(choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms', 'Ms')], max_length=30),
        ),
    ]