
from rest_framework import viewsets
from .models import NoteInfo
from .serializers import NoteSerializer

# Create your views here.

class NoteViewSet(viewsets.ModelViewSet):
    queryset= NoteInfo.objects.all()
    serializer_class=NoteSerializer
