from django.db import models


class Property(models.Model):
    """
    Property model for storing property listing information.
    """
    title = models.CharField(max_length=200, help_text="Property title/name")
    description = models.TextField(help_text="Detailed description of the property")
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        help_text="Property price in USD"
    )
    location = models.CharField(max_length=100, help_text="Property location/address")
    created_at = models.DateTimeField(auto_now_add=True, help_text="When the property was listed")
    
    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"
        ordering = ['-created_at']  # Show newest properties first
    
    def __str__(self):
        return f"{self.title} - ${self.price}"
