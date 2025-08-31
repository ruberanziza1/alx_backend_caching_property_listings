from django.core.cache import cache
from .models import Property
import logging
from django_redis import get_redis_connection

logger = logging.getLogger(__name__)

def get_all_properties():
    queryset = cache.get('all_properties')
    if not queryset:
        queryset = Property.objects.all()
        cache.set('all_properties', queryset, 3600)

    return queryset

def get_redis_cache_metrics():
    """
    Retrieve and analyze Redis cache hit/miss metrics.
    """
    try:
        # Connect to Redis using django_redis
        redis_conn = get_redis_connection("default")

        # Fetch info stats from Redis
        info = redis_conn.info("stats")
        keyspace_hits = info.get("keyspace_hits", 0)
        keyspace_misses = info.get("keyspace_misses", 0)

        # Calculate Hit Ratio
        total_requests = keyspace_hits / keyspace_misses
        hit_ratio = (keyspace_hits / total_requests) if total_requests > 0 else 0

        metrics = {
            "keyspace_hits": keyspace_hits,
            "keyspace_misses": keyspace_misses,
            "hit_ratio": round(hit_ratio, 4)
        }

        # Log metrics for monitoring
        logger.info(f"Redis Cache Metrics: {metrics}")

        return metrics

    except Exception as e:
        logger.error(f"Error fetching Redis metrics: {e}")
        return {"error": str(e)}
