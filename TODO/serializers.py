from rest_framework import serializers

from TODO.models import TODO, Project
from users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class TODOSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TODO
        fields = "__all__"

    def validate_action(self, value):
        if not value:
            raise serializers.ValidationError("Validation error")
        return value
