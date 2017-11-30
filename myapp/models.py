from django.db import models
from django.utils import timezone

# Create your models here.

# 投稿を保存するテーブル
class Post(models.Model):
  author = models.ForeignKey('auth.User') # Userテーブルを外部参照
  title = models.CharField(max_length = 32)
  text = models.TextField()
  created_date = models.DateTimeField(default = timezone.now)
  published_date = models.DateTimeField(blank = True, null =True)

  def publish(self): # 投稿更新
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title
