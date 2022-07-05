from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.CharField(default = 'Bienvenido', max_length = 120)
    image = models.ImageField(default = 'default.png')
    
    def __str__(self):
        return f'Nombre: {self.user.first_name} -- Apellido: {self.user.last_name} -- Usuario: {self.user.username} -- '
    
  
  
class Studios(models.Model):
    name = models.CharField(max_length = 40)
    fundation_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(default = 'default.png')
    
    def __str__(self):
        return f'{self.name}'
    
    
      
class Anime(models.Model):
    name = models.CharField(max_length = 40)
    type = models.CharField(max_length = 5, choices = [('MOV','Movie'),('TV','Tv'),('ONA','Ona'),('OVA','Ova')])
    episodes = models.IntegerField()
    relase_date = models.DateField()
    studio = models.ForeignKey(Studios, on_delete = models.CASCADE, related_name = 'studio')
    genres = models.CharField(max_length = 70)
    duration = models.CharField(max_length = 15)
    description = models.TextField()
    backgroun = models.TextField(default = 'Sin Antecedentes')
    image = models.ImageField(default = 'default.png')
    
    def __str__(self):
        return f'Nombre: {self.name} -- Tipo: {self.type} -- Estudio Animador: {self.studio}'
    
class Manga(models.Model):
    name = models.CharField(max_length = 100)
    type = models.CharField(max_length = 5, choices = [('MAN','Manga')])
    volumenes = models.IntegerField()
    published = models.DateField()
    description = models.TextField(default = 'Sin Descripcion')
    background = models.TextField(default = 'Sin Antecedentes')
    status = models.CharField(max_length = 10, choices = [('FIN','Finished'), ('PUB','Publishing')])
    genres = models.CharField(max_length = 100)
    author = models.CharField(max_length = 40)
    image = models.ImageField(default = 'default.png')
    
    def __str__(self):
        return f'Nombre: {self.name} -- Tipo: {self.type} -- Volumenes: {self.volumenes} -- Autor: {self.author}'
    
    
class Notices(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200, default='')
    content = models.TextField()
    image = models.ImageField(default = 'default.png')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    
    class Meta:
        ordering = ['-timestamp']
        
    def __str__(self):
        return self.content
    

    