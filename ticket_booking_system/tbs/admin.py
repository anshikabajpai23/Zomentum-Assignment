from django.contrib import admin
from .models import Ticket, Movie, Person
# Register your models here.
admin.site.register(Ticket)
admin.site.register(Movie)
admin.site.register(Person)