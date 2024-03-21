# Generated by Django 4.1.3 on 2024-03-19 15:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('sales', models.IntegerField(default=0)),
                ('sold', models.IntegerField(default=0)),
                ('product', models.IntegerField(default=0)),
                ('shop', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Thương hiệu',
                'db_table': 'tb_brand',
            },
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('sales', models.IntegerField(default=0)),
                ('sold', models.IntegerField(default=0)),
                ('product', models.IntegerField(default=0)),
                ('shop', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Ngành hàng',
                'db_table': 'tb_industry',
            },
        ),
    ]