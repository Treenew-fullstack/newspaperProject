from django_filters import (FilterSet, ModelChoiceFilter, DateTimeFilter,)
from django.forms import DateTimeInput
from .models import Post, Category


class PostFilter(FilterSet):
    dt_filter = DateTimeFilter(
        field_name='date_creation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%d-%m-%Y',
            attrs={'type': 'datetime-local'},
        )

    )
    category = ModelChoiceFilter(
        field_name='post_category',
        queryset=Category.objects.all(),
        label='Категория',
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }

