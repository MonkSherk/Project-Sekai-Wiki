from django.urls import path
from sekai_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sekai/', views.SekaiWorldListView.as_view(), name='sekai-list'),
    path('sekai/<int:pk>/', views.SekaiWorldDetailView.as_view(), name='sekai-detail'),
    path('groups/', views.GroupListView.as_view(), name='group-list'),
    path('groups/<int:pk>/', views.GroupDetailView.as_view(), name='group-detail'),
    path('characters/', views.CharacterListView.as_view(), name='character-list'),
    path('characters/<int:pk>/', views.CharacterDetailView.as_view(), name='character-detail'),
    path('cards/', views.CardListView.as_view(), name='card-list'),
    path('cards/<int:pk>/', views.CardDetailView.as_view(), name='card-detail'),
    path('songs/', views.SongListView.as_view(), name='song-list'),
    path('songs/<int:pk>/', views.SongDetailView.as_view(), name='song-detail'),
    path('events/', views.EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
]