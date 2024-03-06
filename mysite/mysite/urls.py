from django.contrib import admin
from django.urls import include, path
#Здесь мы импортируем модули,
# необходимые для работы с административной панелью Django (admin)
# и для определения маршрутов (include, path).#

urlpatterns = [
    path("", include("polls.urls")),
    path("admin/", admin.site.urls), #path("polls/", include("polls.urls")):

    # Это означает, что если кто-то обращается по URL,
    # который начинается с "polls/", Django будет искать дополнительные маршруты в приложении
    # "polls.urls". Это позволяет организовать маршруты внутри приложения "polls".
]
#Итак, этот код определяет, как обрабатывать запросы к различным URL-ам в вашем Django-приложении.






