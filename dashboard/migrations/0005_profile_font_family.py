# Generated by Django 5.2 on 2025-05-05 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_profile_background_color_profile_primary_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='font_family',
            field=models.CharField(choices=[('sans', 'Sans (por defecto)'), ('serif', 'Serif'), ('mono', 'Monoespaciada'), ('inter', 'Inter'), ('poppins', 'Poppins'), ('raleway', 'Raleway')], default='sans', max_length=20),
        ),
    ]
