from django.db import models


class Article(models.Model):
    pub_date = models.DateField()
    title = models.CharField(max_length=200)
    intro = models.TextField()
    content_p1 = models.TextField()
    content_p2 = models.TextField()
    content_p3 = models.TextField()


    def __str__(self):
        return self.title


class Comment(models.Model):
    date = models.DateField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField()


    def __str__(self):
        return self.comment
