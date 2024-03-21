from django.db import models
import uuid

# Create your models here.

class Industry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'tb_industry'
        verbose_name = 'Ngành hàng'


class IndustryReport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name='IndustryReport_industry')
    sales = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    product = models.IntegerField(default=0)
    shop = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tb_industry_report'
        verbose_name = 'Báo cáo ngành hàng'


class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'tb_brand'
        verbose_name = 'Thương hiệu'


class BrandReport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='BrandReport_brand')
    sales = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    product = models.IntegerField(default=0)
    shop = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tb_brand_report'
        verbose_name = 'Báo cáo thương hiệu'