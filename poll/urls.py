
from django.urls import path
from . import views 

from .views import (

    savollar,
    savol_detail,
    check_answer,
    create_question,
    create_choice
    # deleteQuestion

) 
app_name = 'poll'
urlpatterns = [
    path('', savollar, name="savollar"),
    path('savol/<int:id>/', savol_detail, name="savol"),
    path('check/<int:variant_id>/', check_answer, name="check_answer"),
    path('create-question/', create_question, name="create"),
    path('delete-question/<int:id>/', views.deleteQuestion,name="delete-question"),
    path('tanlov-yaratish/', create_choice, name="create_choice")
        
]