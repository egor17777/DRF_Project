
from django.urls import path, include

from women.views import *
from rest_framework import routers

#router = routers.SimpleRouter()
#router.register(r'women',WomenViewSet, basename='momen')

urlpatterns = [
    path('women/',WomenAPIList.as_view()),
    path('women/<int:pk>/',WomenAPIUpdate.as_view()),
    path('womendelete/<int:pk>/',WomenAPIDestroy.as_view()),
    #path('', include(router.urls))
    #path('', WomenViewSet.as_view({'get': 'list'})),
    #path('<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
]