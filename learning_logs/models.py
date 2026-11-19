from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Topic(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="topics")
    text = models.CharField("Название темы", max_length=200)
    description = models.TextField("Описание", blank=True)
    date_added = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        ordering = ["-date_added"]
        verbose_name = "тема"
        verbose_name_plural = "темы"

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("topic_detail", args=[self.pk])

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="entries")
    text = models.TextField("Содержание записи")
    date_added = models.DateTimeField("Дата добавления", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        ordering = ["-date_added"]
        verbose_name = "запись"
        verbose_name_plural = "записи"

    def __str__(self):
        return self.text[:60]
