from django.urls import path, include
from .views import UserAPIList, UserAPIUpdate, UserAPIDestroy
from .yasg import urlpatterns as doc_urls


urlpatterns = [
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/users/', UserAPIList.as_view(), name='user-list'),
    path('api/v1/users/<int:pk>/', UserAPIUpdate.as_view(), name='user-detail'),
    path('api/v1/users/del/<int:pk>/', UserAPIDestroy.as_view(), name='user-delete'),
]

urlpatterns += doc_urls