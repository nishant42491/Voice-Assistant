from django.urls import path


from .views import VoiceAssistantInput

urlpatterns = [
path('',VoiceAssistantInput, name='va'),
]

