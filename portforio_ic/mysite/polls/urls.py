from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('monokuro/', views.monokuro, name='monokuro'),
    path('face_checker/', views.face_checker, name='face_checker'),
    path('face_checker/result', views.fc_result, name='fc_result'),
]
