from django.db import models
from django.contrib.auth.models import User

# Create your models here.





class Category(models.Model):
    name = models.CharField(("Kategori Adı"), max_length=50)
    
    def __str__(self):
        return self.name

class Video(models.Model):
    category = models.ManyToManyField(Category, verbose_name=("Kategori"))
    title = models.CharField(("Video Başlığı"), max_length=100)
    image = models.FileField(("Video Resmi"), upload_to='', max_length=100)
    date_now = models.DateTimeField(("Yayın Tarihi"),  auto_now_add=True)
    imdb = models.FloatField(("IMDB"))
    
    def __str__(self):
        return self.title
    
class Profil(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcılar"), on_delete=models.CASCADE)
    name = models.CharField(("İsim"), max_length=50)
    image = models.FileField(("Kullanıcı Resmi"), upload_to='', max_length=100, blank=True, null=True)
    favori = models.ManyToManyField(Video, verbose_name=("Favori Videolar"))
    
    def __str__(self):
        return self.user.username 
    