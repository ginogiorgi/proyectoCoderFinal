from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',homeView, name = 'Home'),
    path('animeData/', animeData, name = 'Anime Data'),
    path('animeDelete/<int:id_anime>/', deleteAnime, name = 'Delete Anime'),
    path('editAnime/<int:id_anime>', editAnime, name = 'Edit Anime'),
    path('mangaData/', mangaData, name = 'Manga Data'),
    path('mangaDelete/<int:id_manga>/', deleteManga, name = 'Delete Manga'),
    path('editManga/<int:id_manga>', editManga, name = 'Edit Manga'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
