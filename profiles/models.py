from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class UserLink(models.Model):
    user = models.ForeignKey(User, related_name='links', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'({self.title} - {self.user.username})'