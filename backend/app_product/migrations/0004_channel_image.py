# Generated by Django 4.1.3 on 2024-03-20 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0003_product_rate_product_rate_count_product_sold'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='image',
            field=models.ImageField(null=True, upload_to='channel'),
        ),
    ]
