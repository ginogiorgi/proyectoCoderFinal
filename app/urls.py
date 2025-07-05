from django.urls import path, include
from core.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View

class LogoutViewGet(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('Login'))

urlpatterns = [
    path('',homeView, name = 'Home'),
    path('animeData/', animeData, name = 'Anime Data'),
    path('animeDelete/<int:id_anime>/', deleteAnime, name = 'Delete Anime'),
    path('editAnime/<int:id_anime>', editAnime, name = 'Edit Anime'),
    path('animeDetails/<int:id_anime>/', animeDetails, name = 'Anime Details'),
    path('mangaData/', mangaData, name = 'Manga Data'),
    path('mangaDelete/<int:id_manga>/', deleteManga, name = 'Delete Manga'),
    path('editManga/<int:id_manga>', editManga, name = 'Edit Manga'),
    path('mangaDetails/<int:id_manga>/', mangaDetails, name = 'Manga Details'),
    path('studioData/', studioData, name = 'Studio Data'),
    path('studioDelete/<int:id_studio>/', deleteStudio, name = 'Delete Studio'),
    path('editStudio/<int:id_studio>', editStudio, name = 'Edit Studio'),
    path('registerUser/', registerUser, name = 'Register'),
    path('loginUser/', loginRequest, name = 'Login'),
    path('logout/', LogoutViewGet.as_view(), name = 'Logout'),
    path('profileDetails/<str:username>/',profile, name = 'Profile'),
    path('editProfile/', editProfile, name = 'Edit Profile'),
    path('animeList/', animeSearch, name = 'Anime Search'),
    path('mangaList/', mangaSearch, name = 'Manga Search'),
    path('studioList/', studioSearch, name = 'Studios Search'),
    path('noticesHome/', noticePost, name = 'Notices'),
    path('noticeDetail/<int:id_notice>/', noticeDetail, name = 'Notice Details'),
    path('createNotice/', createNotice, name = 'New Notice'),
    path('aboutus/', aboutus, name = 'About Us'),
    path('studioDetails/<int:id_studio>/', studioDetails, name = 'Studio Details')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
