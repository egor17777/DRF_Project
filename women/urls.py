
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from women.views import *
from rest_framework import routers

#router = routers.SimpleRouter()
#router.register(r'women',WomenViewSet, basename='momen')

urlpatterns = [
    path('women/',WomenAPIList.as_view()),
    path('women/<int:pk>/',WomenAPIUpdate.as_view()),
    path('womendelete/<int:pk>/',WomenAPIDestroy.as_view()),
    path('drf-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    #path('', include(router.urls))
    #path('', WomenViewSet.as_view({'get': 'list'})),
    #path('<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
]