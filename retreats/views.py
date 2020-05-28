from django.shortcuts import render
from django.views import generic
from retreats.models import Event, Facility
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from PIL import Image

def index(request):
    event_list = Event.objects.order_by('-start_date')[:3]
    context = {'event_list': event_list}

    return render(request, 'index.html', context)

class EventList(generic.ListView):
    model = Event

class EventDetail(generic.DetailView):
    model = Event

class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = '__all__'

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = '__all__'

class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('events')

class FacilityList(LoginRequiredMixin, generic.ListView):
    model = Facility

class FacilityCreate(LoginRequiredMixin, CreateView):
    model = Facility
    fields = '__all__'

class FacilityDetail(LoginRequiredMixin, generic.DetailView):
    model = Facility

class FacilityUpdate(LoginRequiredMixin, UpdateView):
    model = Facility
    fields = '__all__'

class FacilityDelete(LoginRequiredMixin, DeleteView):
    model = Facility
    success_url = reverse_lazy('facilities')

def about(request):
    return render(request, 'about_us.html')

def accomodations(request):
    return render(request, 'accomodations.html')

def our_vision(request):
    return render(request, 'our_vision.html')

def the_space(request):
    return render(request, 'the_space.html')

def the_farm(request):
    return render(request, 'the_farm.html')

def connect(request):
    return render(request, 'connect.html')

def host(request):
    return render(request, 'host.html')
