from rest_framework.viewsets import ModelViewSet

from .models import user
from .serializers import AuthorModelSerializer


class AuthorModelViewSet(ModelViewSet):
    queryset = user.objects.all()
    serializer_class = AuthorModelSerializer
