from django.core.cache import cache
from .models import Property
import logging

logger = logging.getLogger(__name__)

def get_all_properties():
    properties = cache.get('all_properties')
    
    if not properties:
        properties = list(Property.objects.all())
        cache.set('all_properties', properties, 3600)
    
    return properties

def get_redis_cache_metrics():
    """
    Retrieves and analyzes Redis cache hit and miss metrics.
    """
    try:
        redis_cache = cache.get_master_client('default')
        info = redis_cache.info('stats')
        keyspace_hits = info.get('keyspace_hits', 0)
        keyspace_misses = info.get('keyspace_misses', 0)
        
        total_requests = keyspace_hits + keyspace_misses
        hit_ratio = 0
        if total_requests > 0:
            hit_ratio = (keyspace_hits / total_requests) * 100
            
        metrics = {
            'keyspace_hits': keyspace_hits,
            'keyspace_misses': keyspace_misses,
            'total_requests': total_requests,
            'hit_ratio': hit_ratio
        }
        
        logger.info(f"Redis Cache Metrics: Hits={keyspace_hits}, Misses={keyspace_misses}, Hit Ratio={hit_ratio:.2f}%")
        return metrics
    except Exception as e:
        logger.error(f"Failed to retrieve Redis metrics: {e}")
        return {}
