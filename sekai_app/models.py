from django.db import models

class SekaiWorld(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.ImageField(upload_to='sekai_images', blank=True)

    def __str__(self):
        return self.name

    # Получение всех групп, связанных с данным SekaiWorld
    def get_groups(self):
        return self.groups.all()


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='group_images', blank=True)
    sekai = models.ForeignKey(SekaiWorld, on_delete=models.CASCADE, related_name='groups')

    def __str__(self):
        return self.name

    # Получение всех персонажей, связанных с этой группой
    def get_characters(self):
        return self.characters.all()


class Character(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='characters')
    description = models.TextField()
    sekai_type = models.CharField(max_length=255, choices=[
        ('Game Character', 'Game Character'),
        ('Virtual Singer', 'Virtual Singer'),
    ])
    image = models.ImageField(upload_to='character_images', blank=True)

    def __str__(self):
        return self.name

    # Получение всех карточек, связанных с этим персонажем
    def get_cards(self):
        return self.cards.all()


class Card(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='cards')
    rarity = models.CharField(max_length=10, choices=[('1★', '1★'), ('2★', '2★'), ('3★', '3★'), ('4★', '4★'), ('Limited', 'Limited')])
    stats = models.TextField()
    image_url = models.ImageField(upload_to='card_images', blank=True)
    is_limited = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.character.name} - {self.rarity}'


class Song(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    animation = models.URLField(blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True, related_name='songs')
    image = models.ImageField(upload_to='song_images', blank=True)
    song_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images', blank=True)
    start_date = models.DateField()
    end_date = models.BooleanField(default=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True, related_name='events')

    def __str__(self):
        return self.name
