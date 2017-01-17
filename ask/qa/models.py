from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.ForeignKey(User)
    likes = models.CommaSeparatedIntegerField(max_length=255)


class QuestionManager:
    def __init__(self):
        pass

    @staticmethod
    def new():
        return Question.objects.all().order_by('-pk')[:10]

    @staticmethod
    def popular():
        return Question.objects.all().order_by('rating')


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
