from django.core.cache import cache
from django_redis import get_redis_connection
from .models import Property
import logging

logger = logging.getLogger(__name__)

CACHE_TIMEOUT = 3600  # seconds (1 hour)


def get_all_properties():
    """
    Retrieve all properties, cached for 1 hour.
    """
    properties = cache.get("all_properties")

    if properties is None:
        properties = list(
            Property.objects.all().values(
                "id", "title", "description", "price", "location", "created_at"
            )
        )
        cache.set("all_properties", properties, CACHE_TIMEOUT)

    return properties


def get_redis_cache_metrics():
    """
    Retrieve Redis cache hit/miss metrics and calculate hit ratio.
    """
    try:
        redis_conn = get_redis_connection("default")
        info = redis_conn.info("stats")

        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_misses", 0)
        total_requests = hits + misses

        # ✅ inline conditional as required
        hit_ratio = round(hits / total_requests, 2) if total_requests > 0 else 0.0

        metrics = {
            "keyspace_hits": hits,
            "keyspace_misses": misses,
            "total_requests": total_requests,
            "hit_ratio": hit_ratio,
        }

        logger.info(f"Redis Cache Metrics: {metrics}")
        return metrics

    except Exception as e:
        logger.error(f"Error fetching Redis metrics: {e}")
        return {
            "keyspace_hits": 0,
            "keyspace_misses": 0,
            "total_requests": 0,
            "hit_ratio": 0.0,
        }
