#python 3.7.1

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from microblog.models import User, Post

@csrf_exempt
def create_user(request):
    # Implementation for creating a new user
    pass

def get_user(request, user_id):
    # Implementation for retrieving details of a specific user
    pass

@csrf_exempt
def update_user(request, user_id):
    # Implementation for updating details of a specific user
    pass

@csrf_exempt
def create_post(request):
    # Implementation for creating a new post
    pass

def get_post(request, post_id):
    # Implementation for retrieving details of a specific post
    pass

@csrf_exempt
def update_post(request, post_id):
    # Implementation for updating details of a specific post
    pass

def delete_post(request, post_id):
    # Implementation for deleting a specific post
    pass

def list_posts(request):
    # Implementation for listing all posts
    pass
