from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest
from models import Question
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm
from django.contrib import auth


def new(request):
    """

    :type request: HttpRequest
    """
    questions = Question.objects.new()
    return main(request, questions)


def popular(request):
    """

    :type request: HttpRequest
    """
    questions = Question.objects.popular()
    return main(request, questions)


def main(request, questions):
    current_page = int(request.GET.get('page', 1))
    paginator = Paginator(questions, 10)
    page = paginator.page(current_page)

    return render(request, 'main.html', {
        'questions': page,
        'pages': paginator.page_range,
        'current_page': current_page
    })


def question(request, question_id=None):
    """

    :type request: HttpRequest
    """
    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.author = request.user
            answer.save()

    try:
        quest = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404()
    answers = quest.answer_set.all()

    return render(request, 'question.html', {
        'question': quest,
        'answers': answers,
        'answer_form': AnswerForm(),
    })


def ask(request):
    """

    :type request: HttpRequest
    """
    if request.method == 'POST':
        ask_form = AskForm(request.POST)
        if ask_form.is_valid():
            question = ask_form.save(commit=False)
            question.author = request.user
            question.save()
            return HttpResponseRedirect(question.get_url())
    else:
        ask_form = AskForm()

    return render(request, 'form.html', {
        'form': ask_form
    })


def signup(request):
    """

    :type request: HttpRequest
    """
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password'],
        )
    else:
        signup_form = SignupForm()
        response = render(request, 'signup.html', {
            'signup_form': signup_form
        })
        response.set_cookie('sessionid', request.COOKIES['sessionid'])
        return response


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/')

    login_form = LoginForm()
    return render(request, 'login.html', {
        'login_form': login_form
    })


def test(request, *args, **kwargs):
    return HttpResponse('OK')
