from rest_framework.serializers import HyperlinkedModelSerializer
from .models import user


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields = "__all__"
