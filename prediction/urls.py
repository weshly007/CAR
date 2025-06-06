from django.urls import path
from django.contrib import admin
from .views import PredictionView, SentimentAnalysisView, SignUpView, SignInView, UserDetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/signup/',SignUpView.as_view(),name='signup'),
    path('auth/signin/',SignInView.as_view(),name='signin'),
    path('get/quiz/',PredictionView.as_view(),name='predict'),
    path('get/sentiment/', SentimentAnalysisView.as_view(), name='get_sentiment'),
    path('get/user/',UserDetailsView.as_view(),name='user')
]
