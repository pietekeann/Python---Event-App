from django.db import models
from django.urls import reverse

class Facility(models.Model):
    name = models.CharField(max_length=500, help_text='Enter a Description (e.g. Food - Vegetarian Meal')

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
  #  home_image = models.ImageField()
   # header_image = models.ImageField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    short_description = models.TextField(max_length=350, help_text='Enter a short description of the retreat')
    description = models.TextField(max_length=1500, help_text='Enter a description of the retreat')
    facilities = models.ManyToManyField(Facility, help_text='Select the Facilities Present')
    host = models.TextField(max_length=1000, null=True, blank=True, help_text='Enter a description of the facilitator if there is one')
    schedule = models.TextField(max_length=1000, null=True, blank=True, help_text='Enter a description of the schedule if there is one')
    picture_position = models.CharField(max_length=6, default='center')

    class Meta:
        ordering = ['-start_date']
    
    @property
    def is_pastEvent(self):
        return self.end_date < date.today()

    @property
    def months_different(self):
        return self.start_date.strftime('%B') == self.end_date.strftime('%B')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])
    
    def display_type(self):
        return ', '.join(type.name for type in self. type.all()[:3])
        display_type.short_description = 'Facility'