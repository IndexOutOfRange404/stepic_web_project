from django.contrib.auth.models import User
from django.db import models


class QuestionManager(models.Manager):
    @staticmethod
    def new():
        return Question.objects.all().order_by('-pk')[:10]

    @staticmethod
    def popular():
        return Question.objects.all().order_by('rating')


class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.ForeignKey(User, default=None, null=True, related_name='question_author')
    likes = models.ManyToManyField(User)
    objects = QuestionManager()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
