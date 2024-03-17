from rest_framework import viewsets
from .serializer import SerieSerializer
from .models import Serie

class SerieView(viewsets.ModelViewSet):
  serializer_class = SerieSerializer
  queryset = Serie.objects.all()
