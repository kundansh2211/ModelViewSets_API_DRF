from rest_framework.response import Response
from .serializers import MobileSerializer
from .models import Mobile
from rest_framework.viewsets import  ModelViewSet

class MobileViewSet(ModelViewSet):
    serializer_class = MobileSerializer
    queryset = Mobile.objects.all()

