from rest_framework import serializers
from .models import Conversation, Message
from users.serializers import UserProfileSerializer


class ConversationSerializer(serializers.ModelSerializer):
    user1 = UserProfileSerializer(read_only=True)
    user2 = serializers.PrimaryKeyRelatedField(queryset=None)

    class Meta:
        model = Conversation
        fields = ["id", "user1", "user2", "created_at"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # user2 must be ANY valid user
        from users.models import UserProfile
        self.fields["user2"].queryset = UserProfile.objects.all()


class MessageSerializer(serializers.ModelSerializer):
    sender = UserProfileSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ["id", "conversation", "sender", "content", "created_at"]
        read_only_fields = ["conversation"]