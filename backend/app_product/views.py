from .serializers import *

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class ChannelView(APIView):
    def get(self, request):
        channel = Channel.objects.all()
        return Response(ChannelSerializer(channel, many=True).data, status=200)

    def post(self, request):
        serializer = ChannelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)


class ChannelDetailView(APIView):
    def get(self, request, id):
        try:
            channel = Channel.objects.get(id=id)
            return Response(ChannelSerializer(channel).data, status=200)
        except Exception as e:
            return Response(str(e), status=400)

    def delete(self, request, id):
        try:
            Channel.objects.get(id=id).delete()
            return Response("Delete successful", status=200)
        except Exception as e:
            return Response(str(e), status=400)
    
    def patch(self, request, id):
        channel = Channel.objects.get(id=id)
        serizlizer = ChannelSerializer(channel, data=request.data, partial=True)
        if serizlizer.is_valid():
            serizlizer.save()
            return Response(serizlizer.data, status=200)
        else:
            return Response(serizlizer.errors, status=400)
    

class ProductView(APIView):
    def get(self, request):
        all = request.query_params.get('all')
        if not all:
            product = Product.objects.all()
            pagination = PageNumberPagination()
            page = pagination.paginate_queryset(product, request)
            serializer = ProductSerializer(page, many=True)
            return pagination.get_paginated_response(serializer.data)
        else:
            product = Product.objects.all()
            serializer = ProductSerializer(product, many=True)
            return Response(serializer.data, status=200)

    def post(self, request):
        serializer = ProductSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)


class ProductDetailView(APIView):
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
            return Response(ProductSerializer(product).data, status=200)
        except Exception as e:
            return Response(str(e), status=400)

    def delete(self, request, id):
        try:
            Product.objects.get(id=id).delete()
            return Response("Delete successful", status=200)
        except Exception as e:
            return Response(str(e), status=400)
    
    def patch(self, request, id):
        name = request.data.get('name')
        description = request.data.get('description')
        channel = request.data.get('channel')
        rate = request.data.get('rate')
        rate_count = request.data.get('rate_count')
        sold = request.data.get('sold')

        product = Product.objects.get(id=id)
        if name:
            product.name = name
        if description:
            product.description = description
        if rate:
            product.rate = rate
        if rate_count:
            product.rate_count = rate_count
        if sold:
            product.sold = sold
        if channel:
            product.channel = Channel.objects.get(id=channel)
        product.save()
        return Response(ProductSerializer(product).data, status=200)
    

class ProductImageView(APIView):
    def get(self, request, id):
        product_image = ProductImage.objects.filter(product=id)
        serializer = ProductImageSerializer(product_image, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, id):
        serializer = ProductImageSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)
    
    def delete(self, request, id):
        try:
            image_id = request.query_params.get('image')
            ProductImage.objects.get(id=image_id).delete()
            return Response("delete successful", status=200)
        except Exception as e:
            return Response(str(e), status=400)
        

class PriceView(APIView):
    def get(self, request, id):
        price = Price.objects.filter(product=id)
        pagination = PageNumberPagination()
        page = pagination.paginate_queryset(price, request)
        serializer = PriceSerializer(page, many=True)
        return pagination.get_paginated_response(serializer.data)
    
    def post(self, request, id):
        serializer = PriceSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)


class RateView(APIView):
    def get(self, request, id):
        rate = Rate.objects.filter(product=id)
        pagination = PageNumberPagination()
        page = pagination.paginate_queryset(rate, request)
        serializer = RateSerializer(page, many=True)
        return pagination.get_paginated_response(serializer.data)
    
    def post(self, request, id):
        serializer = RateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)


class RateMediaView(APIView):
    def get(self, request, id):
        rate_media = RateMedia.objects.filter(rate=id)
        serializer = RateMediaSerializer(rate_media, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, id):
        serializer = RateMediaSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)
    
    def delete(self, request, id):
        try:
            image_id = request.query_params.get('image')
            RateMedia.objects.get(id=image_id).delete()
            return Response("Delete successful", status=200)
        except Exception as e:
            return Response(str(e), status=400)