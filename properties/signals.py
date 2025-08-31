from .models import Property
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.core.cache import cache

@receiver(post_save, sender=Property)
def invalidate_cache_on_save(sender, instance, created, **kwargs):
    # Invalidate cache on create or update
    cache.delete('all_properties')
    
@receiver(post_delete, sender=Property)
def invalidate_cache_on_delete(sender, instance, **kwargs):
    # Invalidate cache on delete
    cache.delete('all_properties')