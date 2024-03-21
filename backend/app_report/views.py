from .serializers import *
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class IndustryView(APIView):
    def get(self, request):
        industry = Industry.objects.all()
        pagination = PageNumberPagination()
        page = pagination.paginate_queryset(industry, request)
        serializer = IndustrySerializer(page, many=True)
        return pagination.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = IndustrySerializer(
            data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)


class IndustryReportView(APIView):
    def get(self, request):
        all = request.query_params.get('all')
        if not all:
            industry_report = IndustryReport.objects.all()
            pagination = PageNumberPagination()
            page = pagination.paginate_queryset(industry_report, request)
            serializer = IndustryReportSerializer(page, many=True)
            return pagination.get_paginated_response(serializer.data)
        else:
            industry_report = IndustryReport.objects.all()
            serializer = IndustryReportSerializer(industry_report, many=True)
            return Response(serializer.data, status=200)

    def post(self, request):
        serializer = IndustryReportSerializer(
            data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)


class BrandView(APIView):
    def get(self, request):
        brand = Brand.objects.all()
        pagination = PageNumberPagination()
        page = pagination.paginate_queryset(brand, request)
        serializer = BrandSerializer(page, many=True)
        return pagination.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = BrandSerializer(
            data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)


class BrandReportView(APIView):
    def get(self, request):
        all = request.query_params.get('all')
        if not all:
            brand_report = BrandReport.objects.all()
            pagination = PageNumberPagination()
            page = pagination.paginate_queryset(brand_report, request)
            serializer = BrandReportSerializer(page, many=True)
            return pagination.get_paginated_response(serializer.data)
        else:
            brand_report = BrandReport.objects.all()
            serializer = BrandReportSerializer(brand_report, many=True)
            return Response(serializer.data, status=200)

    def post(self, request):
        serializer = BrandReportSerializer(
            data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)


@api_view(['GET'])
def getIndustryStatistical(request):
    industry = Industry.objects.all()
    results = []
    for i in industry:
        industry_report = {
            "industry": {
                "id": str(i.id),
                "name": i.name
            },
            "sales": 0,
            "sold": 0,
            "product": 0,
            "shop": 0,
        }
        report = IndustryReport.objects.filter(industry=i)
        for j in report:
            industry_report['sales'] += j.sales
            industry_report['sold'] += j.sold
            industry_report['product'] += j.product
            industry_report['shop'] += j.shop
        results.append(industry_report)
    return Response(results, status=200)


@api_view(['GET'])
def getBrandStatistical(request):
    brand = Brand.objects.all()
    results = []
    for i in brand:
        brand_report = {
            "brand": {
                "id": str(i.id),
                "name": i.name
            },
            "sales": 0,
            "sold": 0,
            "product": 0,
            "shop": 0,
        }
        report = BrandReport.objects.filter(brand=i)
        for j in report:
            brand_report['sales'] += j.sales
            brand_report['sold'] += j.sold
            brand_report['product'] += j.product
            brand_report['shop'] += j.shop
        results.append(brand_report)
    return Response(results, status=200)
