from django.shortcuts import render,redirect, HttpResponseRedirect
from .models import *


# Create your views here.

def index(request):
    return render(request,'index.html')

def browse(request):
    profiller = Profil.objects.filter(user=request.user)
    profil_len = len(list(profiller))
    if profil_len <= 3:
        if request.method == "POST":
        # print(request.POST)
        # print(request.FILES)
            try:
                profilname = request.POST["profilname"]
                profilimg = request.FILES["profilimg"]
                print(profilimg)
                
                profil = Profil(name=profilname, image=profilimg, user=request.user)
                profil.save()
                return redirect('browse')
            except:
                profilname = request.POST["profilname"]

                profil = Profil(name=profilname,  user=request.user)
                profil.save()
                return redirect('browse')
    else:
        context = {
            "hata":"Profil sayın en fazla 4 olabilir!",
            "profiller": profiller,
        }
        return render(request, 'browse.html', context)
    
    context = {
        "profiller": profiller,
    }
        
    return render(request,'browse.html',context)

def browseIndex(request,id,name='all'):
    profil = Profil.objects.get(id=id)
    video = Video.objects.all()

    if name == 'Diziler':
        video = Video.objects.filter(category=3)
    elif name == 'Filmler':
        video = Video.objects.filter(category=4)
    elif name == 'Yeni':
        video = Video.objects.filter(category=5)
    elif name == 'Listem':
        video = profil.favori.all()
        # print("PROFIL LİSTEM!!!!!!!!!!!!",profil.favori.all())
        # profil.favori.add(2)  # manytomany içerisinde akleme yapar
        # profil.favori.set([1,2])  # manytomany güncelleme
        # profil.favori.remove(2) # manytomany çıkarma
        
    if request.method == "POST":
        print("=====POST=====",request.POST)
        
        # video = Video.objects.filter(id=profil.favori)
    
    
    context = {
        "profil":profil,
        "video": video,
    }
    
    return render(request,'browse-index.html',context)

def hesap(request):
    return render(request,'users/hesap.html')

def listeAdd(request,proid, vid):
    profil = Profil.objects.get(id=proid)
    # video = Video.objects.get(id = vid)
    profil.favori.add(vid)
    
    return HttpResponseRedirect('/browseIndex/{}/Listem/'.format(proid))

def listeRemove(request,proid,vid):
    profil = Profil.objects.get(id=proid)
    # video = Video.objects.get(id = vid)
    profil.favori.remove(vid)

    return HttpResponseRedirect('/browseIndex/{}/Listem/'.format(proid))
    