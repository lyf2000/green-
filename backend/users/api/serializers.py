from rest_framework import serializers
from users.models import User


class OtherUserSerializer(serializers.ModelSerializer):
    is_friend = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'is_friend')

    def get_is_friend(self, obj):
        request = self.context['request']
        value = 'true'
        if obj.pk == request.user.pk:
            value = 'null'
        elif obj.pk not in request.user.follow.all().values_list('id', flat=True):
            value = 'false'
        return value
