from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name='title')
    text = models.TextField(verbose_name='post')
    posted_by = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    picture = models.ImageField(upload_to='post_pictures/', blank=True)

    def __str__(self):
        return '{}: {}'.format(self.posted_by, self.title)

    def text_len(self):
        return len(self.text)

    def comments_quantity(self):
        return self.comment_set.count()

    def get_absolute_url(self):
        pass ## TODO: После создания поста ты должен автоматически переходить по его url


class Comment(models.Model):
    text = models.TextField(verbose_name='comment text')
    posted_by = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}: {}'.format(self.posted_by, self.post.title, self.text)
