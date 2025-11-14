from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import NoteViewSet

router=DefaultRouter()

router.register('notes',NoteViewSet,basename='note')

urlpatterns = [
    path('',include(router.urls)),
]