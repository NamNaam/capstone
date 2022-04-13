from django.urls import path
from . import views

app_name = 'conc'
urlpatterns = [
    path('', views.index, name='index'),
    path('project/', views.project, name='project'),
    path('detect/', views.detect, name='detect'),
    path('result/', views.result, name='result'),
    path('mypage/', views.mypage.as_view(), name='mypage'),
    path('StartWebcam/', views.StartWebcam, name='StartWebcam'),
    path('predict/', views.predict, name='predict'),
]