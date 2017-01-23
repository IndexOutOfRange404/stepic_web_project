from django.contrib.auth.models import User
from django.db import models


class QuestionManager(models.Manager):
    def new(self):
        return self.all().order_by('-pk')

    def popular(self):
        return self.all().order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True, related_name='question_author')
    likes = models.ManyToManyField(User)
    objects = QuestionManager()

    def get_url(self):
        return "/question/{}/".format(self.pk)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, blank=True, null=True)
