from django.contrib import admin
from pages.models import PageTypeModel, PageContentModel

admin.site.register(PageTypeModel)
admin.site.register(PageContentModel)
