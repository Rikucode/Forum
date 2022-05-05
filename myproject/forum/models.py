import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    pass


class Theme(models.Model):
    themeTitle = models.CharField(verbose_name='Название', max_length=255)
    themeText = models.TextField(verbose_name='Описание')
    themeDate = models.DateTimeField(verbose_name='Дата создания')
    themeUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    is_active = models.BooleanField(default=False, verbose_name='Одобрено?')

    def __str__(self):
        return self.themeTitle


class Topic(models.Model):
    topicTheme = models.ForeignKey(Theme, on_delete=models.CASCADE, verbose_name='Тема топика')
    topicTitle = models.CharField(verbose_name='Название', max_length=255)
    topicText = models.TextField(verbose_name='Текст топика')
    topicDate = models.DateTimeField(verbose_name='Дата публикации')
    topicUser = models.CharField(max_length=150, verbose_name='Пользователь')

    def __str__(self):
        return self.topicTitle


class Answer(models.Model):
    answerUser = models.CharField(max_length=150, verbose_name='Пользователь')
    answerTopic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Вопрос')
    answerDate = models.DateTimeField(verbose_name='Дата написания ответа')
    answerText = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.answerText



