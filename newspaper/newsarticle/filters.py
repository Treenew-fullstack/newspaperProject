from django_filters import (FilterSet, DateTimeFilter, ModelMultipleChoiceFilter, MultipleChoiceFilter)
from django.forms import DateTimeInput
from .models import Post, Category

# Словарь типов категорий для фильтации
STATUS_CHOICES = Post.CATEGORY_CHOICES

# Фильтр для поиска статей
class PostFilter(FilterSet):
    # Фильтр по дате (от даты и свежее) с календарем
    dt_filter = DateTimeFilter(
        field_name='date_creation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%d-%m-%Y',
            attrs={'type': 'datetime-local'},
        )

    )
    # Поле фильтрации по категориям
    category = ModelMultipleChoiceFilter(
        field_name='post_category',
        queryset=Category.objects.all(),
        label='Категория',
    )
    # Поле фильтрации по типам категорий
    category_type = MultipleChoiceFilter(
        choices=STATUS_CHOICES,
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }
