from django.urls import include, path

from posts.views import PostList, PostRetriveDestroy, VoteCreate

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostRetriveDestroy.as_view()),
    path('posts/<int:pk>/vote', VoteCreate.as_view()),
]
