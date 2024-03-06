from django.http import HttpResponse  # это класс в Django, предназначенный для создания HTTP-ответов.
from django.shortcuts import redirect

"""
 Этот класс может быть использован для возвращения простых текстовых ответов,
 HTML-страниц, JSON-данных и других видов содержимого.
"""


def index(request):  # объясняю свою функцию
    return HttpResponse(
        "Дима пошел нахуй")  # Когда кто-то обращается к URL, который связан с этой функцией представления (view),
    # Django вызывает эту функцию, передавая HTTP-запрос.
    # Функция создает и возвращает объект HttpResponse,
    # который отправляется обратно клиенту в качестве HTTP-ответа.


def home(request):
    return redirect('/polls')


