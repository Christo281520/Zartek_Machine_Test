from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, RideSerializer
from .models import Ride
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        ride = self.get_object()
        status = request.data.get('status')

        if status not in ['requested', 'started', 'completed', 'cancelled']:
            return Response({'error': 'Invalid status'})

        ride.status = status
        ride.save()
        return Response({
            'message': 'Status updated successfully',
            'new_status': ride.status
        })

    @action(detail=True, methods=['post'])
    def accept_ride(self, request, pk=None):
        ride = self.get_object()
        ride.driver = ride.rider
        ride.status = 'started'
        ride.save()
        return Response({
            'message': 'Ride accepted successfully',
            'driver': ride.driver.username,
            'status': ride.status
        })

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'username': token.user.username
        })