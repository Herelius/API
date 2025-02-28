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
