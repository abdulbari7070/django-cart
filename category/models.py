from django.db import models


class Category(models.Model):
    parent = models.ForeignKey(
        'self', 
        related_name='category_children', 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True
    )
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        full_path = [self.title]                  
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' > '.join(full_path[::-1])
            
            
            