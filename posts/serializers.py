from rest_framework import serializers

from posts.models import Post, Vote

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    author_id = serializers.ReadOnlyField(source='author.id')
    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'author', 'author_id', 'created']


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']
