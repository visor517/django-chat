from django.db import models

class Message(models.Model):
    message_author = models.CharField('автор', max_length = 20)
    message_text = models.TextField('сообщение')
    message_time = models.DateTimeField('время отправки')

    def __str__(self):
        return self.message_text

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'