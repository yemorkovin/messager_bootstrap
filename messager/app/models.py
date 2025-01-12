from django.db import models

class User(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='users_avatar')
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)


class Chat(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    avatar = models.ImageField(upload_to='chats_avatar')
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='chat_user')
    created_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    text = models.TextField()
    file = models.FileField(upload_to='chats_files', default=None)
    image = models.ImageField(upload_to='chats_img', default=None)
    created_at = models.DateTimeField(auto_now=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
