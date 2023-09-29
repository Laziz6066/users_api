import django_filters
from .models import UserProfile


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = UserProfile
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'icontains'],
            'phone_num': ['exact', 'icontains']
        }
