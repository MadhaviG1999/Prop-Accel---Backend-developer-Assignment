#python 3.7.1

from django.urls import path
from microblog.views import (
    create_user,
    get_user,
    update_user,
    create_post,
    get_post,
    update_post,
    delete_post,
    list_posts,
)

urlpatterns = [
    path('api/users/', create_user, name='create_user'),
    path('api/users/<int:user_id>/', get_user, name='get_user'),
    path('api/users/<int:user_id>/', update_user, name='update_user'),
    path('api/posts/', create_post, name='create_post'),
    path('api/posts/<int:post_id>/', get_post, name='get_post'),
    path('api/posts/<int:post_id>/', update_post, name='update_post'),
    path('api/posts/<int:post_id>/', delete_post, name='delete_post'),
    path('api/posts/', list
