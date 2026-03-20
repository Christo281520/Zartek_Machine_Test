from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, RideSerializer
from .models import Ride
from rest_framework.decorators import action
from rest_framework.response import Response

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