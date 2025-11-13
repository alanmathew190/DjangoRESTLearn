from rest_framework import serializers
from .models import NoteInfo

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=NoteInfo
        fields=['id','title','content']