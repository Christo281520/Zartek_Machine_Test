from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, RideViewSet

router = DefaultRouter()
router.register('rides', RideViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('', include(router.urls)),
]