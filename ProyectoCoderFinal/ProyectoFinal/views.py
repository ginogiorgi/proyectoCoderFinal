from django.shortcuts import redirect, render
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