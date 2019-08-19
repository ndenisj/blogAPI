from .serializers import BlogPostSerializer
from blog.models import BlogPost
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class BlogList(generics.ListAPIView):
    lookup_field = 'pk'
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAdminUser]