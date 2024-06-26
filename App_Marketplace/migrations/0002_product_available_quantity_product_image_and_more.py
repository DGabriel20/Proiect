# Generated by Django 4.2.7 on 2024-02-22 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='ingredients',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='weight_grams',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
