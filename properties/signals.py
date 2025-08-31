from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Property
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Property)
@receiver(post_delete, sender=Property)
def invalidate_property_cache(sender, instance, **kwargs):
    """
    Invalidates the 'all_properties' cache key on property save or delete.
    """
    cache.delete('all_properties')
    logger.info("Cache for 'all_properties' has been invalidated.")
