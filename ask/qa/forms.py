from django.contrib.auth.models import User
from django.forms import ModelForm

from qa.models import Question, Answer


class AskForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question']


class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
