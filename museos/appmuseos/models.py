from django.db import models
from django.contrib.auth.models import User
    
class Museum(models.Model):
    name=models.CharField(max_length=32, unique=True)
    description=models.TextField(null=True)
    horary=models.TextField(null=True)
    transport=models.TextField(default="No Data", null=True)
    address=models.TextField(null=True)
    barrio=models.CharField(max_length=32, null=True)
    district=models.CharField(max_length=32, null=True)
    number_phone=models.TextField(null=True)
    mail=models.TextField(null=True)
    accessibility=models.NullBooleanField(default=False,null=True)
    url=models.TextField(null=True)
 
    num_likes=models.IntegerField(default=0)
    user_likes=models.ManyToManyField(User)
    
    def __str__(self):
        return(self.name)
    
class Coment(models.Model):
    usuario = models.ForeignKey(User)
    museum = models.ForeignKey(Museum)
    title=models.CharField(max_length=64, default="Título")
    text=models.TextField(default="Comentario")
    
class Configuracion_user(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    size= models.IntegerField(null=True, blank=True)
    color=models.CharField(max_length=32, null=True, blank=True)
    
    def __str__(self):
        return self.user.username
        
class Page_user(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)        
    page=models.CharField(max_length=64, null=True,blank=True)
    
    def __str__(self):
        return self.page    
        
class Meta:
    ordering=('district')

    
