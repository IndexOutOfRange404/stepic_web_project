from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest
from models import Question


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
    try:
        quest = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404()
    answers = quest.answer_set.all()

    return render(request, 'question.html', {
        'question': quest,
        'answers': answers
    })


def test(request, *args, **kwargs):
    return HttpResponse('OK')
