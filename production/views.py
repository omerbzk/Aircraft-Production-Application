from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from .models import Team, Personnel, AircraftType, Part, Aircraft
from .serializers import TeamSerializer, PersonnelSerializer, AircraftTypeSerializer, PartSerializer, AircraftSerializer

@login_required
def home(request):
    return render(request, 'production/home.html')

@login_required
def part_list(request):
    try:
        parts = Part.objects.all()
        return render(request, 'production/part_list.html', {'parts': parts})
    except Exception as e:
        print(e)
        return render(request, 'production/error.html', {'error': str(e)})

@login_required
def aircraft_list(request):
    try:
        aircrafts = Aircraft.objects.all()
        aircraft_types = AircraftType.objects.all()
        parts = Part.objects.all()
        user_team = request.user.personnel.team.name if hasattr(request.user, 'personnel') else None
        print(user_team)
        return render(request, 'production/aircraft_list.html', {
            'aircrafts': aircrafts,
            'aircraft_types': aircraft_types,
            'parts': parts,
            'user_team': user_team
        })
    except Exception as e:
        print(e)
        return render(request, 'production/error.html', {'error': str(e)})
@login_required
def aircrafttype_list(request):
    try:
        aircraft_types = AircraftType.objects.all()
        return render(request, 'production/aircrafttype_list.html', {'aircraft_types': aircraft_types})
    except Exception as e:
        print(e)
        return render(request, 'production/error.html', {'error': str(e)})

@login_required
def personnel_list(request):
    try:
        personnels = Personnel.objects.all()
        return render(request, 'production/personnel_list.html', {'personnels': personnels})
    except Exception as e:
        print(e)
        return render(request, 'production/error.html', {'error': str(e)})

@login_required
def team_list(request):
    try:
        teams = Team.objects.all()
        return render(request, 'production/team_list.html', {'teams': teams})
    except Exception as e:
        print(e)
        return render(request, 'production/error.html', {'error': str(e)})

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]

class PersonnelViewSet(viewsets.ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    permission_classes = [permissions.IsAuthenticated]

class AircraftTypeViewSet(viewsets.ModelViewSet):
    queryset = AircraftType.objects.all()
    serializer_class = AircraftTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        personnel = self.request.user.personnel
        part_type = serializer.validated_data['type']
        
        team_part_mapping = {
            'WING': 'WING',
            'BODY': 'BODY',
            'TAIL': 'TAIL',
            'AVIONICS': 'AVIONICS'
        }
        
        if personnel.team.name != team_part_mapping.get(part_type):
            raise permissions.PermissionDenied("Bu parçayı üretme yetkiniz yok.")
            
        serializer.save(created_by=personnel)

class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        personnel = self.request.user.personnel
        
        if personnel.team.name != 'ASSEMBLY':
            raise permissions.PermissionDenied("Sadece montaj takımı uçak üretebilir.")
            
        aircraft_type = serializer.validated_data['aircraft_type']
        parts = [
            serializer.validated_data['wing'],
            serializer.validated_data['body'],
            serializer.validated_data['tail'],
            serializer.validated_data['avionics']
        ]
        
        for part in parts:
            if part.aircraft_type != aircraft_type:
                raise serializers.ValidationError("Uyumsuz parçalar.")
            if part.is_used:
                raise serializers.ValidationError("Bu parça zaten kullanılmış.")
                
        for part in parts:
            part.is_used = True
            part.save()
            
        serializer.save(assembled_by=personnel)