from rest_framework import serializers
from .models import *


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    channel = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'
    
    def create(self, validated_data):
        request = self.context.get('request')
        channel = request.data.get('channel')

        validated_data['channel'] = Channel.objects.get(id=channel)
        product = Product(**validated_data)
        product.save()
        return product

    def get_channel(self, obj):
        return ChannelSerializer(obj.channel).data
    
    def get_price(self, obj):
        try:
            price = Price.objects.filter(product=obj).first()
            return price.display_price
        except:
            return None
    
    def get_image(self, obj):
        try:
            image = ProductImage.objects.filter(product=obj).first()
            return image.image.url
        except:
            return None


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
    
    def create(self, validated_data):
        request = self.context.get('request')
        product = request.data.get('product')

        validated_data['product'] = Product.objects.get(id=product)
        product_image = ProductImage(**validated_data)
        product_image.save()
        return product_image


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Rate
        fields = '__all__'
    
    def get_image(self, obj):
        results = []
        for i in RateMedia.objects.filter(rate=obj):
            results.append(i.image.url)
        return results


class RateMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateMedia
        fields = '__all__'