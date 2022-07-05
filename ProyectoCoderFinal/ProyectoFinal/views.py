import re
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import *
from .forms import *

def homeView(request):
    notices = Notices.objects.all()
    mangas = Manga.objects.all()
    animes = Anime.objects.all()
    mangas_list = []
    anime_list = []
    notice_list = []
    
    for i in mangas:
        if len(mangas_list) == 4:
            break
        mangas_list.append(i)
    
    for i in animes:
        if len(anime_list) == 4:
            break
        anime_list.append(i)
        
    for i in notices:
        if len(notice_list) == 3:
            break
        notice_list.append(i)
        
    context = {'notices':notice_list, 'mangas': mangas_list, 'animes': anime_list}
        
    return render(request, 'proyectofinal/base.html', context)

#CRUD Anime

def animeData(request):
    
    animes = Anime.objects.all()
    
    if request.method == 'POST':     
        form = AnimeForm(request.POST,request.FILES)
            
        if form.is_valid():   
            form.save()
            return redirect('Anime Data')

    else:
        form = AnimeForm()

    context = {'animes':animes,'form':form}
    
    return render(request, 'proyectofinal/animeData.html', context)

def deleteAnime(request, id_anime):
    
    anime = Anime.objects.filter(id = id_anime)
    anime.delete()
    messages.success(request, 'Anime Eliminado')
    
    return redirect('Anime Data')
    
def editAnime(request, id_anime):
    
    anime = Anime.objects.get(id = id_anime)
     
    if request.method == 'POST':
        form = AnimeForm(request.POST,request.FILES, instance = anime)
        
        if form.is_valid():
            form.save()
            
            return redirect('Anime Data')
    else:
        form = AnimeForm(instance = anime)
    
    context = {'form': form, 'anime': anime}
    
    return render(request, 'proyectofinal/editAnime.html', context)
    
#CRUD Manga

def mangaData(request):
    
    mangas = Manga.objects.all()
    
    if request.method == 'POST':
        form = MangaForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('Manga Data')

    else:
        form = MangaForm()

    context = {'mangas': mangas, 'form': form}
    
    return render(request, 'proyectofinal/mangaData.html', context)

def deleteManga(request, id_manga):
    
    manga = Manga.objects.filter(id = id_manga)
    manga.delete()
    messages.success(request, 'Anime Eliminado')
    
    return redirect('Manga Data')

def editManga(request, id_manga):
    
    manga = Manga.objects.get(id = id_manga)
     
    if request.method == 'POST':
        form = MangaForm(request.POST,request.FILES, instance = manga)
        
        if form.is_valid():
            form.save()
            
            return redirect('Manga Data')
    else:
        form = MangaForm(instance = manga)
    
    context = {'form': form, 'manga': manga}
    
    return render(request, 'proyectofinal/editManga.html', context)

#CRUD Studio

def studioData(request):
    
    studios = Studios.objects.all()
    
    if request.method == 'POST':
        form = StudiosForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            
            return redirect('Studio Data')
    
    else:
        form = StudiosForm()
        
    context = {'form': form, 'studios': studios}
    
    return render(request, 'proyectofinal/studioData.html', context)

def deleteStudio(request, id_studio):
    
    studio = Studios.objects.filter(id = id_studio)
    studio.delete()
    messages.success(request, 'Studio Eliminado')
    
    return redirect('Studio Data')

def editStudio(request, id_studio):
    
    studio = Studios.objects.get(id = id_studio)
     
    if request.method == 'POST':
        form = StudiosForm(request.POST,request.FILES, instance = studio)
        
        if form.is_valid():
            form.save()
            
            return redirect('Studio Data')
        
    else:
        form = StudiosForm(instance = studio)
    
    context = {'form': form, 'studio': studio}
    
    return render(request, 'proyectofinal/editStudio.html', context)

#REGISTER, LOGIN AND LOGOUT

def registerUser(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            profile = Profile()
            profile.user = user
            profile.save()
            request.user = user
            
            return redirect('Home')
    
    else:
        form = UserRegisterForm()
    
    context = {'form': form}
    
    return render(request, 'proyectofinal/registerUser.html', context)

def loginRequest(request):
    
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate (username = username, password = password)
            
            if user is not None:
                login(request, user)
                 
                return redirect('Home')
        else:
            form = LoginForm()
            return render (request, 'proyectofinal/loginUser.html', {'form': form, 'message': 'Username or Password incorrect'})
        
    else:
        form = LoginForm()
        return render (request, 'proyectofinal/loginUser.html', {'form': form})

#PROFILE AND EDIT PROFILE

def profile(request):
    return render(request, 'proyectofinal/profileDetails.html')

def editProfile(request):
    user = request.user
    
    if request.method == 'POST':
        u_form = UserEditForm(request.POST, instance = request.user)
        p_form = ProfileEditForm(request.POST, request.FILES, instance = user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            
            u_form.cleaned_data
            user.password1 = u_form['password1']
            user.password2 = u_form['password2']
            
            u_form.save()
            p_form.save()
            
            return redirect('Home')
    
    else:
        u_form = UserEditForm(instance = request.user)
        p_form = ProfileEditForm()
        
    context = {'u_form':u_form, 'p_form':p_form}
    
    return render(request, 'proyectofinal/editProfile.html', context)

#LISTS AND GETS

def animeSearch(request):
    
    if request.GET:
        anime_search = request.GET['name']
        animes = Anime.objects.filter(name__icontains = anime_search)
    else:
        animes = Anime.objects.all()
    
    context = {'animes': animes}
    return render(request, 'proyectofinal/animeList.html',context)

def mangaSearch(request):
    
    if request.GET:
        manga_search = request.GET['name']
        mangas = Manga.objects.filter(name__icontains = manga_search)
    else:
        mangas = Manga.objects.all()
    
    context = {'mangas': mangas}
    return render(request, 'proyectofinal/mangaList.html',context)

def studioSearch(request):
    
    if request.GET:
        studio_search = request.GET['name']
        studios = Studios.objects.filter(name__icontains = studio_search)
    else:
        studios = Studios.objects.all()
    
    context = {'studios': studios}
    return render(request, 'proyectofinal/studiosList.html',context)

def noticePost(request):
    notices = Notices.objects.all()
    
    context = {'notices':notices}
    
    return render(request, 'proyectofinal/noticesHome.html', context)

def noticeDetail(request, id_notice):
    notice = Notices.objects.get(id = id_notice)
    
    context = {'notice': notice}
    return render(request, 'proyectofinal/noticeDetail.html', context)

def createNotice(request):
    
    if request.method == 'POST':
        form = NoticesForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            
            return redirect('Notices')
        
    else:
        form = NoticesForm()
    
    context = {'form':form}
    
    return render(request, 'proyectofinal/createNotice.html', context)