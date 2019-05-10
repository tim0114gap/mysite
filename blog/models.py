import  datetime
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    image = models.ImageField(upload_to='images/')
    text = models.TextField()

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title
