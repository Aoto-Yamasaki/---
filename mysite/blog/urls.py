from django.urls import path
from . import views

urlpatterns = [
     path('step1/', views.step1_view, name='step1'),
    path('step2/', views.step2_view, name='step2'),
      path('questionnaire/', views.questionnaire_view, name='questionnaire'),
      path('result/', views.result_view, name ='result')

    # path('', views.home, name='home'),
]