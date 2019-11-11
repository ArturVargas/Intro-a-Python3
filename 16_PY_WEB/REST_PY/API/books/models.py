from django.db import models

# Create your models here.
class Libro(models.Model):
  author = models.CharField(max_length=35)
  isbn = models.CharField(max_length=15)
  page_num = models.IntegerField()
  avaliable = models.BooleanField()
  created_at = models.DateTimeField(auto_now_add=True)

#Esta funcion nos regresará el nombre del autor
  def __str__(self):
    return self.author
