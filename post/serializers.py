from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Post
        fields = ('url','id','created','name','user')
        extra_kwargs ={
            'url':{
                'view_name':'post:post-detail',
            }
        }
