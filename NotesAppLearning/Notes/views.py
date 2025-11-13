from django.http import JsonResponse
from .models import NoteInfo
from .serializers import NoteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def print_hello(request):
    if request.method=='GET':
        notes=NoteInfo.objects.all()
        serializers=NoteSerializer(notes,many=True)
        return JsonResponse(serializers.data)
    
    elif request.method=='POST':
        serializers=NoteSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
