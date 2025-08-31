from django.shortcuts import render
from django.http import JsonResponse
from .models import Property
from django.views.decorators.cache import cache_page
from .utils import get_all_properties, get_redis_cache_metrics

@cache_page(60 * 15)
def property_list(request):
    properties_queryset = get_all_properties()
    return JsonResponse({'data': list(properties_queryset)})

def cache_metrics_view(request):
    metrics = get_redis_cache_metrics()
    return JsonResponse(metrics)
