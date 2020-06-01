from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.EventList.as_view(), name='events'),
    path('events/<int:pk>', views.EventDetail.as_view(), name='event-detail'),
    path('facilities/', views.FacilityList.as_view(), name='facilities'),
]

urlpatterns += [  
    path('about', views.about, name='about_us'),
    path('accomodations', views.accomodations, name='accomodations'),
    path('our-vision', views.our_vision, name='our_vision'),
    path('the-space', views.the_space, name='the_space'),
    path('the-farm', views.the_farm, name='the_farm'),
    path('connect', views.connect, name='connect'),
    path('host-retreat', views.host, name='host'),
]

urlpatterns += [  
    path('event/create/', views.EventCreate.as_view(), name='event_create'),
    path('event/<int:pk>/update/', views.EventUpdate.as_view(), name='event_update'),
    path('event/<int:pk>/delete/', views.EventDelete.as_view(), name='event_delete'),
]

urlpatterns += [  
    path('facility/create/', views.FacilityCreate.as_view(), name='facility_create'),
    path('facility/<int:pk>/update/', views.FacilityUpdate.as_view(), name='facility_update'),
    path('facility/<int:pk>/delete/', views.FacilityDelete.as_view(), name='facility_delete'),
]
