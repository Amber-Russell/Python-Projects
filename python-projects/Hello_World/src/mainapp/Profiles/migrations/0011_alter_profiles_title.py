# Generated by Django 3.2.6 on 2021-08-20 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0010_alter_profiles_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='title',
            field=models.CharField(choices=[('Ms', 'Ms'), ('Mrs.', 'Mrs.'), ('Mr.', 'Mr.')], max_length=30),
        ),
    ]