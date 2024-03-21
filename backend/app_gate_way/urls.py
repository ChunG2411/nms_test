from django.urls import path
from app_product.views import (
    ChannelView, ChannelDetailView,
    ProductView, ProductDetailView,
    ProductImageView,
    PriceView,
    RateView, RateMediaView
)
from app_report.views import (
    IndustryView, BrandView,
    IndustryReportView, BrandReportView,
    getIndustryStatistical, getBrandStatistical
)

urlpatterns = [
    path('channel', ChannelView.as_view(), name='ChannelView'),
    path('channel/<str:id>', ChannelDetailView.as_view(), name='ChannelDetailView'),

    path('product', ProductView.as_view(), name='ProductView'),
    path('product/<str:id>', ProductDetailView.as_view(), name='ProductDetailView'),

    path('product/image/<str:id>', ProductImageView.as_view(), name='ProductImageView'),
    path('product/price/<str:id>', PriceView.as_view(), name='PriceView'),
    path('product/rate/<str:id>', RateView.as_view(), name='RateView'),

    path('rate/media/<str:id>', RateMediaView.as_view(), name='RateMediaView'),

    path('industry', IndustryView.as_view(), name='IndustryView'),
    path('brand', BrandView.as_view(), name='BrandView'),
    path('industry/report', IndustryReportView.as_view(), name='IndustryReportView'),
    path('brand/report', BrandReportView.as_view(), name='BrandReportView'),
    path('industry/statistical', getIndustryStatistical, name='getIndustryStatistical'),
    path('brand/statistical', getBrandStatistical, name='getBrandStatistical'),

]
