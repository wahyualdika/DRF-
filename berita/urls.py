from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.BeritaList.as_view()),
    path('<int:pk>/', views.BeritaDetail.as_view(),name='berita-detail'),
    path('user/<int:pk>',views.UserDetail.as_view(),name='user-detail'),
    path('tipe_berita/<int:pk>',views.TipeBeritaDetail.as_view(),name='tipe-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
