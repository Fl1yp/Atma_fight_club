from django.db import models
from django.utils import timezone


class Main(models.Model):
    title = models.CharField(verbose_name="Название", max_length=100)
    description = models.CharField(verbose_name="Описание", max_length=100)

    def __str__(self):
        return f"{self.title}, {self.description}"


class Contact(models.Model):
    name = models.CharField(max_length=12, verbose_name="Имя", )
    number = models.CharField(verbose_name="Номер", max_length=15)
    date = models.DateTimeField(default=timezone.now())

    def save(self, *args, **kwargs):
        self.date = self.date.replace(microsecond=0)  # обрезаем миллисекунды
        super(Contact, self).save(*args, **kwargs)

    def __str__(self):
        return f"\n Время:{self.date} \n id:{self.id}\n Имя:{self.name}\n Номер:{self.number}\n\n"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


class Photo(models.Model):
    img = models.ImageField(verbose_name="Фото")

    def __str__(self):
        return f"{self.img}"

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"


class Question(models.Model):
    question = models.CharField(max_length=150, verbose_name="Вопрос", )
    answer = models.CharField(max_length=400, verbose_name="Ответ", )

    def __str__(self):
        return f"{self.question}"

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
