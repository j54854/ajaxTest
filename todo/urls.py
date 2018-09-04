from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "todo"

urlpatterns = [
    path('step3/', TemplateView.as_view(template_name='todo/step3.html'), name='step3'),
    path('step4/', views.step4, name='step4'),
    path('step5/', TemplateView.as_view(template_name='todo/step5.html'), name='step5'),
    path('step6/', TemplateView.as_view(template_name='todo/step6.html'), name='step6'),
    path('step7/', TemplateView.as_view(template_name='todo/step7.html'), name='step7'),
    path('step<str:num>/', views.step1or2, name='step1or2'),
    path('get/', views.get_todo, name='get_todo'),
    path('post/', views.post_todo, name='post_todo'),
]
