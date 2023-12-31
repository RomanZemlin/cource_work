from django.db import models

from users.models import User


# Create your models here.


class Message(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Содержание письма')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'


class EmailDistribution(models.Model):
    emails = models.ManyToManyField('Client', verbose_name='Клиенты')
    start = models.DateTimeField(verbose_name='Дата начала рассылки')
    next = models.DateTimeField(verbose_name='Дата следующей попытки', null=True, blank=True)
    finish = models.DateTimeField(verbose_name='Дата окончания рассылки')
    period = models.CharField(max_length=255, choices=[('1', 'Раз в день'), ('2', 'Раз в неделю'), ('3', 'Раз в месяц')],
                              default='1', verbose_name='Период рассылки')
    status = models.PositiveSmallIntegerField(default=1, verbose_name='Статус рассылки')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение', default=None)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.emails} ({self.start} - {self.finish})'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Logs(models.Model):
    time = models.DateTimeField(verbose_name='Дата и время последней попытки', default=None)
    mailing = models.ForeignKey(EmailDistribution, on_delete=models.CASCADE, verbose_name='Рассылка')
    mail = models.EmailField(max_length=100, verbose_name='Почта', null=True, blank=True)
    response = models.BooleanField(default=False, verbose_name='Ответ почтового сервера', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.time} - {self.response}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя клиента")
    email = models.EmailField(max_length=100, verbose_name="Почта")
    comment = models.TextField(verbose_name="Комментарий", null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.name} ({self.email})'

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"