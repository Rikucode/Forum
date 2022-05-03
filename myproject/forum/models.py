import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    pass

class Question(models.Model):
    qTitle = models.CharField(verbose_name='Название', max_length=255)
    qText = models.TextField(verbose_name='Вопрос')
    qDate = models.DateTimeField(verbose_name='Дата публикации')
    qUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    def __str__(self):
        return self.qTitle

    def wasPublishedRecently(self):
        return self.qDate >= timezone.now() - datetime.timedelta(days=1)


class Answer(models.Model):
    answerUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    answerQuestion = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    answerDate = models.DateTimeField(verbose_name='Дата написания ответа')
    answerText = models.TextField(verbose_name='Ответ')
    answerVotes = models.IntegerField(default=0,verbose_name='Рейтинг')

    def __str__(self):
        return self.answerText



