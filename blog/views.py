from django.shortcuts import render
from rest_framework import viewsets,permissions,status
from .models import Blog, Tag
from django.contrib.auth.models import User
from .serializers import BlogSerializers, TagSerializers, UserBlogSerializers, CreateBlogSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def userDetail(request,pk):
    user = User.objects.get(pk=pk)
    if request.user.id != user.id:
        return Response({"response":"You don't have permission on this item"})
    serializer_context = {
        'request': request,
    }
    serializers = UserBlogSerializers(user,context=serializer_context)
    return Response(serializers.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def insertPost(request):
    serializer = CreateBlogSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def blog(request):
    user = request.user
    blog = Blog.objects.filter(author = user)
    serializer_context = {
        'request': request,
    }
    serializers = BlogSerializers(blog,many=True,context=serializer_context)
    return Response(serializers.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def blogList(request):
    blog = Blog.objects.all()
    serializer_context = {
        'request': request,
    }
    serializers = BlogSerializers(blog,many=True,context=serializer_context)
    return Response(serializers.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def userBlog(request,pk):
    blog = Blog.objects.get(pk=pk)
    if request.user != blog.author:
        return Response({"response":"Don't have permission on this object"})
    serializer_context = {
        'request': request,
    }
    serializers = BlogSerializers(blog,context=serializer_context)
    return Response(serializers.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def tagDetail(request,pk):
    tag = Tag.objects.get(pk=pk)
    serializer_context = {
        'request': request,
    }
    serializers = TagSerializers(tag,context=serializer_context)
    return Response(serializers.data)

@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def updateBlog(request,pk):
    blog = Blog.objects.get(pk=pk)
    if request.user != blog.author:
        return Response({"response":"Don't have permission on this object"})
    serializers = CreateBlogSerializers(blog,data = request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def deleteBlog(request,pk):
    blog = Blog.objects.get(pk=pk)
    if request.user != blog.author:
        return Response({"response":"Don't have permission on this object"})
    blog.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
