from rest_framework import serializers
from .models import Post
from taggit_serializer.serializers import TaggitSerializer
from django.contrib.auth.models import User


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):

    # tags = TagListSerializerField()
    author = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ("id", "h1", "title", "slug", "description", "content", "created_at", "author",
                  "tags")
        lookup_fields = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }