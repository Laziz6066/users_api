from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import UserProfile
from .serializers import UserSerializer
from .filters import UserFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.filters import OrderingFilter


class UserAPIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10000


class UserAPIList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = UserAPIListPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = UserFilter
    ordering_fields = ['first_name', 'last_name', 'phone_num']


class UserAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class UserAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly, )
