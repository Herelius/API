from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        # Specify the content of the model that we want the api to return
        fields = ["id", "title", "content", "published_date"]