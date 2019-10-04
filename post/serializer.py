from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Post
        # fields = '__all__' # 전부를 Serializer 에서 사용할 때는 이렇게 하면됨
        fields = ['id','title', 'body']
        write_only_fields = ('title',)
