from django.urls import path

from .views import LogsView,LogDetailView
 

urlpatterns = [
    path('logs/', LogsView.as_view()),
    path('logs/<int:pk>', LogDetailView.as_view()),
]
