from django.db import models

from levelupapi.models.event_gamer import Event_Gamer
class Event(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    description = models.CharField(max_length=100) 
    date = models.DateField(auto_now_add=True) 
    time = models.TimeField(auto_now_add=True)
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    attendees = models.ManyToManyField("Gamer", through="Event_Gamer", related_name="attending") 
    
    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value