"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from mysite.views import HomeView
from mysite.views import UserCreateView, UserCreateDoneTV   # 회원가입처리를 수행하는 뷰
# from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # 장고 전용 인증 URLconf : django.contrib.auth.urls (/login/, /logout/, /password_change/)
    path('accounts/register/', UserCreateView.as_view(), name='register'), # 회원가입
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'), # 회원가입 완료
    path('', HomeView.as_view(), name='home'),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
    path('photo/', include('photo.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
