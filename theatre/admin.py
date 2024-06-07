from django.contrib import admin
from .models import (
    Ticket,
    Play,
    Actor,
    Genre,
    TheatreHall,
    Performance,
    Reservation,
)

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Play)
admin.site.register(TheatreHall)
admin.site.register(Performance)
admin.site.register(Reservation)
