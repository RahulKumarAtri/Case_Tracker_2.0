from django.urls import path
from . import views

app_name = 'cases'
urlpatterns = [
    path('', views.index, name='index'),
    path('track', views.track, name='track'),
    path('compare', views.compare, name='compare'),
    path('final', views.final, name='final')
]