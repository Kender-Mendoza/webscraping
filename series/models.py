from django.db import models

class Serie(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=20)
  pic_img = models.CharField(max_length=200)
  state = models.CharField(max_length=20)
  chapters_number = models.IntegerField(default=0)
  donwloaded_times = models.IntegerField(default=0)
  favorite = models.BooleanField(default=False)

  def __str__(self):
    return self.name
