from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    target_type = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'actor_username', 'verb', 'target_type', 'timestamp', 'is_read']

    def get_target_type(self, obj):
        return str(obj.target)  # Shows a simple representation of the target object