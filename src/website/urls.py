from django.urls import path

from .views import HomeView, ImageListView, ImageDetailView, StartSession, SessionListView

app_name = 'website'
urlpatterns = [
    path('', SessionListView.as_view(), name='session-list'),
    path('session/<int:pk>/', ImageListView.as_view(), name='session-detail-list'),
    path('<int:pk>/', HomeView.as_view(), name='home-pk'),
    path('image/', HomeView.as_view(), name='home'),
    path('image/<int:pk>/', ImageDetailView.as_view(), name='scan-image-detail'),
    path('start/session/', StartSession.as_view(), name='start-session'),
]
