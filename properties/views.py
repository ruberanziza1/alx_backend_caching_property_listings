from django.shortcuts import render
from .utils import get_all_properties
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)  # Cache the view for 15 minutes
def property_list(request):
    properties = get_all_properties()
    context = {
        'properties': properties
    }
    return render(request, 'properties/property_list.html', context)
