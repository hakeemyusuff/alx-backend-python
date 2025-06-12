import django_filters
from .models import Message


class MessageFilter(django_filters.Filterset):
    sender = django_filters.CharFilter(
        field_name="sender__first_name",
        lookup_expr="iexact",
    )
    created_after = django_filters.DateTimeFilter(
        field_name="created_at",
        lookup_expr="gte",
    )
    created_before = django_filters.DateTimeFilter(
        field_name="created_at",
        lookup_expr="lte",
    )
    
    class Meta:
        model = Message
        fields = ["sender", "created_after", "created_before"]
