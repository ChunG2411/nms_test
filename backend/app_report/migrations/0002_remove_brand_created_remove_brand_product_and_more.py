# Generated by Django 4.1.3 on 2024-03-19 15:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app_report', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='created',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='product',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='sales',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='shop',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='sold',
        ),
        migrations.RemoveField(
            model_name='industry',
            name='created',
        ),
        migrations.RemoveField(
            model_name='industry',
            name='product',
        ),
        migrations.RemoveField(
            model_name='industry',
            name='sales',
        ),
        migrations.RemoveField(
            model_name='industry',
            name='shop',
        ),
        migrations.RemoveField(
            model_name='industry',
            name='sold',
        ),
        migrations.CreateModel(
            name='IndustryReport',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('sales', models.IntegerField(default=0)),
                ('sold', models.IntegerField(default=0)),
                ('product', models.IntegerField(default=0)),
                ('shop', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='IndustryReport_industry', to='app_report.industry')),
            ],
            options={
                'verbose_name': 'Báo cáo ngành hàng',
                'db_table': 'tb_industry_report',
            },
        ),
        migrations.CreateModel(
            name='BrandReport',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('sales', models.IntegerField(default=0)),
                ('sold', models.IntegerField(default=0)),
                ('product', models.IntegerField(default=0)),
                ('shop', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BrandReport_brand', to='app_report.brand')),
            ],
            options={
                'verbose_name': 'Báo cáo thương hiệu',
                'db_table': 'tb_brand_report',
            },
        ),
    ]
