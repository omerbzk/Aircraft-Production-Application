from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    TEAM_CHOICES = [
        ('WING', 'Kanat Takımı'),
        ('BODY', 'Gövde Takımı'),
        ('TAIL', 'Kuyruk Takımı'),
        ('AVIONICS', 'Aviyonik Takımı'),
        ('ASSEMBLY', 'Montaj Takımı'),
    ]
    
    name = models.CharField(max_length=50, choices=TEAM_CHOICES)
    
    def __str__(self):
        return self.get_name_display()

class Personnel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} - {self.team}"

class AircraftType(models.Model):
    AIRCRAFT_CHOICES = [
        ('TB2', 'TB2'),
        ('TB3', 'TB3'),
        ('AKINCI', 'AKINCI'),
        ('KIZILELMA', 'KIZILELMA'),
    ]
    
    name = models.CharField(max_length=50, choices=AIRCRAFT_CHOICES)
    
    def __str__(self):
        return self.get_name_display()

class Part(models.Model):
    PART_TYPES = [
        ('WING', 'Kanat'),
        ('BODY', 'Gövde'),
        ('TAIL', 'Kuyruk'),
        ('AVIONICS', 'Aviyonik'),
    ]
    
    type = models.CharField(max_length=50, choices=PART_TYPES)
    aircraft_type = models.ForeignKey(AircraftType, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.get_type_display()} - {self.aircraft_type}"

class Aircraft(models.Model):
    aircraft_type = models.ForeignKey(AircraftType, on_delete=models.CASCADE)
    wing = models.OneToOneField(Part, related_name='aircraft_wing', on_delete=models.CASCADE)
    body = models.OneToOneField(Part, related_name='aircraft_body', on_delete=models.CASCADE)
    tail = models.OneToOneField(Part, related_name='aircraft_tail', on_delete=models.CASCADE)
    avionics = models.OneToOneField(Part, related_name='aircraft_avionics', on_delete=models.CASCADE)
    assembled_by = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    assembled_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.aircraft_type} - {self.id}"