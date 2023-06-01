from django.urls import path
from .views import GetInfoView, download_info

app_name = 'restapi'    

urlpatterns = [
    path('api/', GetInfoView.as_view(), name='get_info'),
    path('api/download/', download_info, name='download_info'),
]
