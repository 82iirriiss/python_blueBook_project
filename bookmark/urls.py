from django.urls import path
from bookmark import views as v

app_name = 'bookmark'
urlpatterns = [
        path('', v.BookmarkLV.as_view(), name='index'),
        path('<int:pk>/', v.BookmarkDV.as_view(), name='detail'),
        path('add/', v.BookmarkCreateView.as_view(), name='add'),
        path('change/', v.BookmarkChangeLV.as_view(), name='change'),
        path('<int:pk>/update/', v.BookmarkUpdateView.as_view(), name='update'),
        path('<int:pk>/delete/', v.BookmarkDeleteView.as_view(), name='delete'),
        ]
