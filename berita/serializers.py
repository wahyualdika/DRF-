from rest_framework import serializers
from .models import Berita, TipeBerita
from django.contrib.auth.models import User

class BeritaSerializers(serializers.ModelSerializer):
    #this field will be filled with list of owner of berita
    author = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='user-detail'
    )

    #this field will be filled with berita's type
    tipe_berita = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='tipe-detail'
    )
    class Meta:
        model = Berita
        fields = ('id','title','content','author','tipe_berita')

class CreateBeritaSerializers(serializers.ModelSerializer):
    #using current logged in user id to populate author field
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Berita
        fields = ('id','title','content','author','tipe_berita')

class UserBeritaSerializers(serializers.ModelSerializer):
    #this field will be filled with list of owner's berita
    news = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='berita-detail',
    )

    class Meta:
        model = User
        fields = ('id','username','email','first_name','last_name','news')

class TipeBeritaSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipeBerita
        fields = ('id','name')
