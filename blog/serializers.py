from rest_framework import serializers
from .models import Blog, Tag
from django.contrib.auth.models import User

class BlogSerializers(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='blog-user-detail'
    )

    tags = serializers.HyperlinkedRelatedField(
        many = True,
        read_only=True,
        view_name='tag-detail'
    )
    class Meta:
        model = Blog
        fields = ('id','title','content','author','tags')

class CreateBlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id','title','content','author','tags')

class UserBlogSerializers(serializers.ModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='blog-detail',
    )

    class Meta:
        model = User
        fields = ('id','username','email','first_name','last_name','post')

class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','name')
