# Generated by Django 4.2.10 on 2024-03-04 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_ability_alter_attribute_name_alter_hero_attack_type_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ability',
            options={'verbose_name': 'ability', 'verbose_name_plural': 'abilities'},
        ),
        migrations.AddField(
            model_name='hero',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='hero_images/', verbose_name='Hero Image'),
        ),
    ]