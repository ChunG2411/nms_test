from django.db import models
import uuid
import os

# Create your models here.
def product_upload_to(instance, filename):
    unique_filename = str(uuid.uuid4().hex)
    _, extension = os.path.splitext(filename)

    upload_path = os.path.join('product', str(instance.product.id), unique_filename + extension)
    return upload_path

def rate_upload_to(instance, filename):
    unique_filename = str(uuid.uuid4().hex)
    _, extension = os.path.splitext(filename)

    upload_path = os.path.join('rate', str(instance.rate.id), unique_filename + extension)
    return upload_path


class Channel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    image = models.ImageField(upload_to='channel', null=True)

    class Meta:
        db_table = 'tb_channel'
        verbose_name = 'Kênh bán hàng'


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='Product_channel')
    description = models.TextField(default='')
    rate = models.FloatField(default=0)
    rate_count = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)

    class Meta:
        db_table = 'tb_product'
        verbose_name = 'Sản phẩm'


class ProductImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ProductImage_product')
    image = models.ImageField(upload_to=product_upload_to)

    class Meta:
        db_table = 'tb_product_image'
        verbose_name = 'Hình ảnh sản phẩm'


class Price(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Price_product')
    price = models.IntegerField(default=0)
    display_price = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tb_price'
        verbose_name = 'Giá bán'
        ordering = ["-created"]


class Rate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Rate_product')
    rate = models.IntegerField(default=0)
    content = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tb_rate'
        verbose_name = 'Đánh giá'


class RateMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE, related_name='RateMedia_rate')
    image = models.ImageField(upload_to=rate_upload_to)

    class Meta:
        db_table = 'tb_rate_image'
        verbose_name = 'Hình ảnh đánh giá'