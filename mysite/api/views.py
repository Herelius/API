from django.shortcuts import render
# generics contains generic views to update delete, etc..., any type of model
from rest_framework import generics

from .models import BlogPost
from .serializer import BlogPostSerializer

# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    # Get all the BlogPost that exists
    queryset = BlogPost.objects.all()
    # Specify the serilizer
    serializer_class = BlogPostSerializer
