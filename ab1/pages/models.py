from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class PageTypeModel(models.Model):
    response_code = models.CharField(max_length=255)   
    http_status_code = models.PositiveIntegerField()
    user = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            related_name='page_types',
                            related_query_name='page_types_user_field')
    created_at = models.DateTimeField(name="created_at", verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(name="updated_at", verbose_name="Updated At", auto_now=True)
    

    class Meta:
        verbose_name = _("Page Type")
        verbose_name_plural = _("Page Types")

class PageContentModel(models.Model):
    user = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            related_name='page_contents',
                            related_query_name='review_user_field')
    title = models.CharField(max_length=255)
    content = RichTextField()
    created_at = models.DateTimeField(name="created_at", verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(name="updated_at", verbose_name="Updated At", auto_now=True)
  
    status = models.BooleanField(default=False)
    page_type = models.OneToOneField(
        PageTypeModel,
        on_delete=models.SET_NULL,  
        related_name='page_content',
        verbose_name="Page Type",
        null=True  
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'page_review'
        ordering = ['-created_at']
        verbose_name = _("Page Content")
        verbose_name_plural = _("Page Contents")
