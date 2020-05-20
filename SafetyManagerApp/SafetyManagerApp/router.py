from django.urls import path

from logs.views import LogsView,LogDetailView
 
from equipments.views import EquipmentsView
 

urlpatterns = [
    path('equipments/', EquipmentsView.as_view()),
    path('equipments/<int:pk>', EquipmentsView.as_view()),
    path('logs/', LogsView.as_view()),
    path('logs/<int:pk>', LogDetailView.as_view()),
    path('equipments/', EquipmentsView.as_view()),
    path('equipments/<int:pk>', EquipmentsView.as_view()),
]

