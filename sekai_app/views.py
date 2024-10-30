from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import SekaiWorld, Group, Character, Card, Song, Event
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Home Page
def home(request):
    return render(request, 'sekai_app/home.html')

# SEKAI Worlds
class SekaiWorldListView(ListView):
    model = SekaiWorld
    template_name = 'sekai_app/sekai_worlds.html'
    context_object_name = 'sekai_worlds'

class SekaiWorldDetailView(DetailView):
    model = SekaiWorld
    template_name = 'sekai_app/sekai_world_detail.html'
    context_object_name = 'sekai_world'

# Group Views
class GroupListView(ListView):
    model = Group
    template_name = 'sekai_app/groups.html'
    context_object_name = 'groups'

class GroupDetailView(DetailView):
    model = Group
    template_name = 'sekai_app/group_detail.html'
    context_object_name = 'group'

# Character Views
class CharacterListView(ListView):
    model = Character
    template_name = 'sekai_app/characters.html'
    context_object_name = 'characters'

class CharacterDetailView(DetailView):
    model = Character
    template_name = 'sekai_app/character_detail.html'
    context_object_name = 'character'

# Card Views
class CardListView(ListView):
    model = Card
    template_name = 'sekai_app/cards.html'
    context_object_name = 'cards'

class CardDetailView(DetailView):
    model = Card
    template_name = 'sekai_app/card_detail.html'
    context_object_name = 'card'

# Song Views
class SongListView(ListView):
    model = Song
    template_name = 'sekai_app/songs.html'
    context_object_name = 'songs'

class SongDetailView(DetailView):
    model = Song
    template_name = 'sekai_app/song_detail.html'
    context_object_name = 'song'

# Event Views
class EventListView(ListView):
    model = Event
    template_name = 'sekai_app/events.html'
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    template_name = 'sekai_app/event_detail.html'
    context_object_name = 'event'