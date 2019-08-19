from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def blog_list(request):
    context = {
        'title': 'Blog Post 1',
        'description': 'This is a detailed description based on the title above.'
    }
    return JsonResponse(context)