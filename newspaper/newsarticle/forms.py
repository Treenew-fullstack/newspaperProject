from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'post_category',
            'category_type',
            'text',
        ]


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'post_category',
            'text',

        ]
