from django.urls import path

from .views import EquipmentsView,EquipmentsDetailView
 

urlpatterns = [
    path('equipments/', EquipmentsView.as_view()),
    path('equipments/<int:pk>', EquipmentsView.as_view()),
]
