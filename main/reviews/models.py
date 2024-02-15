from django.db import models
from django.urls import reverse


class Reviews(models.Model):
  avatar = models.ImageField(upload_to="reviews", blank=True, null=True, verbose_name="Аватар пользователя")
  name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Имя")
  slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
  date = models.DateTimeField(blank=True, null=True, verbose_name="Дата")
  text = models.TextField(max_length=250, blank=True, null=True, verbose_name="Текст отзыва")
  status = models.BooleanField(default=False, verbose_name="Статус публикации")
  
  class Meta:
    db_table = 'reviews' 
    verbose_name = 'Отзыв'
    verbose_name_plural = "Отзывы"
    ordering = ("-id",)
    
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
        return reverse("reviews_detail", kwargs={"slug": self.slug})
