from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogEditView, BlogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/new', BlogCreateView.as_view(), name='post_new'),
    path('post/<slug:slug>/edit', BlogEditView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<slug:slug>/detail', BlogDetailView.as_view(), name='post_detalhe'),
]