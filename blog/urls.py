from django.urls import path,include
from . import views
from rest_framework import routers

urlpatterns = [
    path('user/<int:pk>',views.userDetail,name="blog-user-detail"),
    path('create',views.insertPost,name="blog-new"),
    path('list/',views.blogList,name="blog-list"),
    path('',views.blog,name="blog"),
    path('<int:pk>/',views.userBlog,name="blog-detail"),
    path('<int:pk>/update',views.updateBlog,name="blog-update"),
    path('<int:pk>/delete',views.deleteBlog,name="blog-delete"),
    path('tags/<int:pk>',views.tagDetail,name="tag-detail"),
]
