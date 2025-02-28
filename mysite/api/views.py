from django.shortcuts import render
# generics contains generic views to update delete, etc..., any type of model
from rest_framework import generics, status
from rest_framework.response import Response

from .models import BlogPost
from .serializer import BlogPostSerializer
from rest_framework.views import APIView

# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    # Get all the BlogPost that exists
    queryset = BlogPost.objects.all()
    # Specify the serilizer
    serializer_class = BlogPostSerializer
    
    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk" # "pk" = primary key (id of the BlogPost in this case)

class BlogPostList(APIView):
    def get(self, request, format=None):
        # Get the title from the query parameters (if none, default to umpty string)
        title = request.query_params.get("title", "")
        
        if title:
            # Filter the queryset based on the title
            blog_posts = BlogPost.objects.filter(title__icontains=title)
        else:
            # If no title is provided, return all blog posts
            blog_posts = BlogPost.objects.all()
        
        serializer = BlogPostSerializer(blog_posts, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
