from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.EventList.as_view(), name='events'),
    path('events/<int:pk>', views.EventDetail.as_view(), name='event-detail'),
]