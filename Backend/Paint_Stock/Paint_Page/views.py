from rest_framework import viewsets
from .models import PaintUser, Paints
from .serializers import PaintUserSerializer

class PaintUserViewSet(viewsets.ModelViewSet):
    queryset = PaintUser.objects.all()
    serializer_class = PaintUserSerializer

class PaintsViewSet(viewsets.ModelViewSet):
    queryset = Paints.objects.all()
    serializer_class = PaintsSerializer