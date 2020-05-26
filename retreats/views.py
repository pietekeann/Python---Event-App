from django.shortcuts import render
from django.views import generic
from retreats.models import Event, Facility


def index(request):
    event_list = Event.objects.order_by('-start_date')[:3]
    context = {'event_list': event_list}

    return render(request, 'index.html', context)


class EventList(generic.ListView):
    model = Event

class EventDetail(generic.DetailView):
    model = Event