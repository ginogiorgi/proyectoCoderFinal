# Vista de detalle de Manga
def mangaDetails(request, id_manga):
    try:
        manga = Manga.objects.get(id=id_manga)
    except Manga.DoesNotExist:
        messages.error(request, 'El manga no existe.')
        return redirect('Manga Search')
    context = {'manga': manga}
    return render(request, 'mangaDetails.html', context)
# Vista de detalle de Anime
def animeDetails(request, id_anime):
    try:
        anime = Anime.objects.get(id=id_anime)
    except Anime.DoesNotExist:
        messages.error(request, 'El anime no existe.')
        return redirect('Anime Search')
    context = {'anime': anime}
    return render(request, 'animeDetails.html', context)
import re
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from app.models import *
from app.forms import *

def homeView(request):
    notices = Notices.objects.all()
    mangas = Manga.objects.all()
    animes = Anime.objects.all()
    mangas_list = []
    anime_list = []
    notice_list = []
    # Top 3 animes y top 2 mangas para el top5
    top5 = []
    for anime in Anime.objects.order_by('-id')[:3]:
        if anime.id:
            top5.append({'obj': anime, 'type': 'anime'})
    for manga in Manga.objects.order_by('-id')[:2]:
        if manga.id:
            top5.append({'obj': manga, 'type': 'manga'})

    toppopular = Anime.objects.order_by('-id')[:10]
    toplonger = Anime.objects.order_by('-episodes')[:10]

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

    if request.GET:
        user_search = request.GET['username']
        users = User.objects.filter(username__icontains = user_search)
        context = {'users':users}
        return render(request, 'profileList.html', context)

    context = {
        'notices': notice_list,
        'mangas': mangas_list,
        'animes': anime_list,
        'toplonger': toplonger,
        'toppopular': toppopular,
        'top5': top5
    }
    return render(request, 'base.html', context)
    return render(request, 'base.html', context)

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
    
    return render(request, 'animeData.html', context)

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
    
    return render(request, 'editAnime.html', context)
    
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
    
    return render(request, 'mangaData.html', context)

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
    
    return render(request, 'editManga.html', context)

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
    
    return render(request, 'studioData.html', context)

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
    
    return render(request, 'editStudio.html', context)

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
    
    return render(request, 'registerUser.html', context)

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
            return render (request, 'loginUser.html', {'form': form, 'message': 'Username or Password incorrect'})
        
    else:
        form = LoginForm()
        return render (request, 'loginUser.html', {'form': form})

#PROFILE AND EDIT PROFILE

def profile(request, username):
    user = User.objects.get(username = username)
      
    context = {'user': user }
    
    return render(request, 'profileDetails.html', context)

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
    
    return render(request, 'editProfile.html', context)

#LISTS AND GETS

def animeSearch(request):
    
    if request.GET:
        anime_search = request.GET['name']
        animes = Anime.objects.filter(name__icontains = anime_search)
    else:
        animes = Anime.objects.all()
    
    context = {'animes': animes}
    return render(request, 'animeList.html', context)

def mangaSearch(request):
    
    if request.GET:
        manga_search = request.GET['name']
        mangas = Manga.objects.filter(name__icontains = manga_search)
    else:
        mangas = Manga.objects.all()
    
    context = {'mangas': mangas}
    return render(request, 'mangaList.html', context)

def studioSearch(request):
    
    if request.GET:
        studio_search = request.GET['name']
        studios = Studios.objects.filter(name__icontains = studio_search)
    else:
        studios = Studios.objects.all()
    
    context = {'studios': studios}
    return render(request, 'studiosList.html', context)

def noticePost(request):
    notices = Notices.objects.all()
    
    context = {'notices':notices}
    
    return render(request, 'noticesHome.html', context)

def noticeDetail(request, id_notice):
    notice = Notices.objects.get(id = id_notice)
    
    context = {'notice': notice}
    return render(request, 'noticeDetail.html', context)

def createNotice(request):
    
    if request.method == 'POST':
        form = NoticesForm(request.POST, request.FILES)
        
        if form.is_valid():
            notice = form.save()
            notice.user = request.user
            notice.save()
            
            return redirect('Notices')
        
    else:
        form = NoticesForm()
    
    context = {'form':form}
    
    return render(request, 'createNotice.html', context)

def aboutus(request):
    return render(request, 'aboutus.html')