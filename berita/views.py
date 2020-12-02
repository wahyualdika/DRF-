from .models import Berita,TipeBerita
from .serializers import BeritaSerializers, UserBeritaSerializers, CreateBeritaSerializers, TipeBeritaSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth.models import User
from berita.permissions import IsOwnerOrReadOnly

class BeritaList(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    def get(self, request, format=None):
        berita = Berita.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = BeritaSerializers(berita, many=True,context=serializer_context)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer_context = {
            'request': request,
        }
        serializer = CreateBeritaSerializers(data=request.data,context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BeritaDetail(APIView):
        permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
        def get_object(self,pk):
            try:
                berita = Berita.objects.get(pk=pk)
                self.check_object_permissions(self.request, berita)
                return berita
            except Exception as e:
                raise Http404

        def get(self, request, pk, format=None):
            queryset = self.get_object(pk)
            serializer_context = {
                'request': request,
            }
            serializer = BeritaSerializers(queryset,context=serializer_context)
            return Response(serializer.data)

        def put(self, request, pk, format=None):
            queryset = self.get_object(pk)
            serializer_context = {
                'request': request,
            }
            serializer = CreateBeritaSerializers(queryset,data=request.data,context=serializer_context)
            # if queryset.author
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            queryset = self.get_object(pk)
            queryset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class TipeBeritaDetail(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    def get_object(self,pk):
        try:
            return TipeBerita.objects.get(pk=pk)
        except Exception as e:
            raise Http404

    def get(self, request, pk, format = None):
        queryset = self.get_object(pk)
        serializer_context = {
            'request': request,
        }
        serializer = TipeBeritaSerializers(queryset,context=serializer_context)
        return Response(serializer.data)

class UserDetail(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except Exception as e:
            raise Http404

    def get(self, request, pk, format = None):
        queryset = self.get_object(pk)
        serializer_context = {
            'request': request,
        }
        serializer = UserBeritaSerializers(queryset,context=serializer_context)
        return Response(serializer.data)
