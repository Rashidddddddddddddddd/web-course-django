from django.urls import path

from .views import news_list, news_detail, create, remove, my_news, my_create

app_name = "new"
urlpatterns = [
    path('', news_list, name="list"),
    path('<int:id>/', news_detail, name="detail"),
    path('yaratish/', create, name="create"),
    path('remove/int:id/', remove, name="remove"),
    path('my-news/', my_news, name="my_news"),
    path('my-create/', my_create, name="my_create"),
]