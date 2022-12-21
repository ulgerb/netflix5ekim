from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


success=None


def logoutUser(request):

    if request.user.is_authenticated:
        logout(request)
    
    return redirect('loginUser')


def registerUser(request):

    if request.method == "POST":
        # rpost = request.POST
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        
        # for k,v in rpost.items():
        #     if k=="check1":
        #         check1 = "on"
        try:
            check1 = request.POST['check1']
        except:
            check1 = "off"
            
        if check1 != "off":
            if password1==password2:
                if User.objects.filter(username=username).exists():
                    hata = "Bu kullanıcı adı başkası tarafından zaten kullanılıyor !"
                    return render(request, 'users/register.html', {'hata': hata})
                else:
                    if User.objects.filter(email=email).exists():
                        hata = "Bu email başkası tarafından zaten kullanılıyor !"
                        return render(request, 'users/register.html',{'hata':hata})
                    else:
                        user = User.objects.create_user(username=username, password=password1,email=email, first_name=name, last_name=surname)
                        user.save()
                        global success
                        success = "Kaydınız başarı ile tamamlanmıştır.."
                        return redirect('loginUser')
            else:
                hata = "Şifreler aynı değil !"
                return render(request, 'users/register.html', {'hata': hata})
        else:
            hata = "Sözleşmeyi onaylayın !"
            return render(request, 'users/register.html', {'hata': hata})
    
    return render(request,'users/register.html')

def loginUser(request):
    context = {}
    if success is not None:
        context = {"success": success}
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(username = username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('browse')
        else:
            hata = "Kullanıcı adı veya şifre hatalı !"
            return render(request, 'users/login.html', {"hata":hata})
        
    return render(request,'users/login.html',context)