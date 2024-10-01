from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Ad(models.Model):
    CATEGORY_CHOICES = [
        ('tanks', 'Танки'),
        ('healers', 'Хилы'),
        ('dps', 'ДД'),
        ('traders', 'Торговцы'),
        ('guild_masters', 'Гилдмастеры'),
        ('quest_givers', 'Квестгиверы'),
        ('blacksmiths', 'Кузнецы'),
        ('leatherworkers', 'Кожевники'),
        ('alchemists', 'Зельевары'),
        ('spell_masters', 'Мастера заклинаний'),
    ]

    title = models.CharField(max_length=256)
    content = RichTextField()
    category = models.CharField(max_length=64, choices=CATEGORY_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Reply(models.Model):
    ad = models.ForeignKey(Ad, related_name='replies',
                           on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies')
    content = models.TextField()  # Текст отклика
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'Отклик от {self.author} на "{self.ad.title}"'


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Сообщение от {self.sender.username} к {self.recipient.username}'


class OneTimeCode(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Код для {self.email}'
