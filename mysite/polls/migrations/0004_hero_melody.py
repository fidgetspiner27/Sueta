# Generated by Django 4.2.10 on 2024-03-04 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_ability_options_hero_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='melody',
            field=models.FileField(blank=True, null=True, upload_to='melodies/', verbose_name='Melody'),
        ),
    ]
