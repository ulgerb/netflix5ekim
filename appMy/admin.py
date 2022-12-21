from django.contrib import admin
from .models import *

# Register your models here.


class ProfilAdmin(admin.ModelAdmin):
    '''Admin View for list'''

    list_display = ('name','id')
    

class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for list'''

    list_display = ('name','id')
    
    
admin.site.register(Profil, ProfilAdmin)
admin.site.register(Category, CategoryAdmin) 
admin.site.register(Video)
