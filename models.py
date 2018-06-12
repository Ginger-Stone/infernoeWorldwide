from django.db import models
from django.utils import timezone
import datetime

class Portfolio(models.Model):
    project_name = models.CharField(max_length=20, default='')
    intro_text = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='portfolio', blank=False)
    project_description = models.CharField(max_length=350, default='')
    date = models.DateField()
    client = models.CharField(max_length=25, default='')
    category = models.CharField(max_length=25, default='')


    class Meta:
        get_latest_by = ('id')
        verbose_name = ('Portfolio')
        verbose_name_plural = ('Porfolios')

   # def was_published_recently(self):
   #     return self.date >= timezone.now() - datetime.timedelta(days=1)
        

    def __str__(self):
        return self.project_name

class Service(models.Model):
    service_name = models.CharField(max_length=60)
    service_description = models.CharField(max_length=350)

    def __str__(self):
        return self.service_name

    class Meta:
        get_latest_by = 'id'
        verbose_name = 'Service1'

class Service2(models.Model):
    service_name = models.CharField(max_length=60)
    service_description = models.CharField(max_length=350)

    def __str__(self):
        return self.service_name

    class Meta:
        get_latest_by = 'id'
        verbose_name = 'Service2'

class Service3(models.Model):
    service_name = models.CharField(max_length=60)
    service_description = models.CharField(max_length=350)

    def __str__(self):
        return self.service_name

    class Meta:
        get_latest_by = 'id'
        verbose_name = 'Service3'

class Event(models.Model):
    date = models.DateTimeField()
    event = models.CharField(max_length=60)
    event_info = models.CharField(max_length=350)
    image = models.ImageField(upload_to='events', blank=False)

    class Meta:
        get_latest_by = 'id'
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.event

class InfernoeTeam(models.Model):
    image = models.ImageField(upload_to='infernoeTeam', blank=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    position = models.CharField(max_length=50)
    instagram_link = models.CharField(max_length=150)
    facebook_link = models.CharField(max_length=150)
    whatsapp_contact = models.CharField(max_length=15)

    class Meta:
        get_latest_by = 'id'
        verbose_name = 'InfernoeTeam'
        verbose_name_plural = 'InfernoeTeam'

    def __str__(self):
        return self.position

