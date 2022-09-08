
from django.urls import path

from women.views import WomenAPIView


urlpatterns = [
    path('', WomenAPIView.as_view()),
    path('<int:pk>/', WomenAPIView.as_view()),
]