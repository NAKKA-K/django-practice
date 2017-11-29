from django.db import models

# Create your models here.

class Post(models.Model):
  author = models.CharField(max_length = 16)
  title = models.CharField(max_length = 32)
  text = models.TextField()
  created_data = models.DateTimeField()
  published_date = models.DateTimeField()

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title
