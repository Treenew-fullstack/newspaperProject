from .models import *
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'category_type', 'date_creation', 'post_category', 'title', 'rating']