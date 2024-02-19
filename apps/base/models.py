from django.db import models

class Feedback(models.Model):
    name = models.CharField(
        max_length=125,
        verbose_name="Ваше Имя",
        null=False,blank=False
    )
    email = models.EmailField(
        max_length=125,
        verbose_name="Ваша Электронная почта",
        null=False,blank=False,
        unique=True
    )
    subject = models.CharField(
        max_length=310,
        verbose_name="Ваш вопрос"
    )
    message = models.TextField(
        max_length=620,
        verbose_name="Текст"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Обратная связь",
        verbose_name_plural = "Обратная связь"