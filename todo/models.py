from django.db import models

from users.models import User


class Task(models.Model):
    name = models.CharField(max_length=40, verbose_name='Имя задачи')
    description = models.CharField(max_length=100, verbose_name='Описание задачи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.BooleanField(default=False, verbose_name='Статус')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', blank=True, null=True)
    deadline = models.DateField(verbose_name='Срок выполнения', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
