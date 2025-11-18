from rest_framework import generics, permissions
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ConversationSerializer

    def get_queryset(self):
        user = self.request.user.userprofile
        return Conversation.objects.filter(user1=user) | Conversation.objects.filter(user2=user)

    def perform_create(self, serializer):
        serializer.save(user1=self.request.user.userprofile)


class MessageListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MessageSerializer

    def get_queryset(self):
        conversation_id = self.kwargs["conversation_id"]
        return Message.objects.filter(conversation_id=conversation_id)

    def perform_create(self, serializer):
        conversation_id = self.kwargs["conversation_id"]
        serializer.save(
            sender=self.request.user.userprofile,
            conversation_id=conversation_id
        )

