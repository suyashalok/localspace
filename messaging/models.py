from django.db import models
from users.models import UserProfile

class Conversation(models.Model):
    user1 = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='conversations_as_user1')
    user2 = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='conversations_as_user2')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user1', 'user2')

    def __str__(self):
        return f"Conversation: {self.user1} & {self.user2}"

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sent_messages')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender}: {self.text[:20]}"
