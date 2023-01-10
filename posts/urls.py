from django.urls import include, path

from posts.views import PostList

urlpatterns = [
    path('posts/', PostList.as_view()),
]
