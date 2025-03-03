from django.urls import path
from .views import FileUploadedView
from django.http import JsonResponse

def api_home(request):
    return JsonResponse({"message": "Welcome to File Upload API"})

urlpatterns =[
    path('',api_home,name='api_home'),
    path('upload/', FileUploadedView.as_view(), name='file-upload'),
]