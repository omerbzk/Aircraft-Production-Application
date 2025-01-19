from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'teams', views.TeamViewSet)
router.register(r'personnel', views.PersonnelViewSet)
router.register(r'aircraft-types', views.AircraftTypeViewSet)
router.register(r'parts', views.PartViewSet)
router.register(r'aircraft', views.AircraftViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('parts/', views.part_list, name='part_list'),
    path('aircraft/', views.aircraft_list, name='aircraft_list'),
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]