from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Fetches all properties from the cache or the database.
    """
    # Try to get data from cache
    properties = cache.get('all_properties')
    
    if not properties:
        # If not in cache, fetch from database
        properties = list(Property.objects.all())
        # Store in cache for 1 hour (3600 seconds)
        cache.set('all_properties', properties, 3600)
    
    return properties
