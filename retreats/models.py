from django.db import models
from django.urls import reverse
from django.core import validators
from django.core.exceptions import ValidationError
from datetime import date


class Facility(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('facilities')

class Image(models.Model):
    image = models.ImageField(upload_to='img/')

class Event(models.Model):
    title = models.CharField(max_length=200)
  #  home_image = models.ImageField()
   # header_image = models.ImageField()
    # image = models.OneToOneField(Image, on_delete=models.CASCADE, help_text='Select an image or upload a new one', null=True)
    home_image = models.ImageField(upload_to='img/', blank=True, default='img/yoga.jpg')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    short_description = models.TextField(max_length=350, help_text='Enter a short description of the retreat')
    description = models.TextField(max_length=1500, help_text='Enter a description of the retreat')
    facilities = models.ManyToManyField(Facility, help_text='Select the Facilities Present', blank=True)
    host = models.TextField(max_length=1000, null=True, blank=True, help_text='Enter a description of the facilitator if there is one')
    schedule = models.TextField(max_length=1000, null=True, blank=True, help_text='Enter a description of the schedule if there is one')
    picture_position = models.CharField(max_length=6, default='center', help_text='Type: up, down, or center to choose header image position ')

    class Meta:
        ordering = ['-start_date']

    def clean(self):
        if self.end_date and self.end_date < self.start_date:
            raise ValidationError("End date should be greater than start date.")

    @property
    def months_different(self):
        if self.end_date:
            return self.start_date.strftime('%B') == self.end_date.strftime('%B')

    @property
    def current_event(self):
        today = date.today()
        if self.end_date:
            return self.end_date >= today
        return self.start_date >= today
    
    @property
    def position(self):
        if self.picture_position == 'up':
            return '25%'
        elif self.picture_position == 'center':
            return 'center'
        elif self.picture_position == 'down':
            return '75%'

    @property
    def past_event(self):
        today = date.today()
        if self.end_date:
            return self.end_date < today
        return self.start_date < today

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])
    
    def display_type(self):
        return ', '.join(type.name for type in self. type.all()[:3])
        display_type.short_description = 'Facility'