# Generated by Django 3.1.3 on 2020-11-30 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PSI', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pss',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
