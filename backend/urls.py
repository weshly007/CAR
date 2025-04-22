from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/', include('prediction.urls')),
    path('api/', include('chatapp.urls')),
    path('api/', include('voiceapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)