# Generated by Django 4.1.3 on 2024-12-14 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixelpioneer', '0004_alter_productcard_price_alter_productcard_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcard',
            name='feature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productcard',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
    ]
