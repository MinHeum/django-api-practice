from rest_framework import viewsets  # viewsets 에 관한 설명은 내가 해줘야됨
from .models import Post
from .serializer import PostSerializer


# CBV 기반으로 작성하기 때문에 class 로 작성

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()  # queryset은 Postdml 모든 object들을 받아온다는 뜻
    serializer_class = PostSerializer
