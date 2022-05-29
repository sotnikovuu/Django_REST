from rest_framework.viewsets import ModelViewSet

from TODO.models import TODO, Project
from TODO.serializers import ProjectSerializer, TODOSerializer
from users.models import User
from users.serializers import UserModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
