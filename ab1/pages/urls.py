from django.urls import path
from .views import PageTypeListCreateView, PageListCreateView

urlpatterns = [
    path('api/page/types/', PageTypeListCreateView.as_view(), name='page-type-list-create'),
    path('api/pages/', PageListCreateView.as_view(), name='page-list-create'),
]
