
from django_filters import FilterSet, DateFilter
from .models import Post, Author

class PostFilter(FilterSet):

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author': ['exact'],
            'created': ['gt'],
        }