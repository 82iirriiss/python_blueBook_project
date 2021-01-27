from django.urls import path, re_path
from blog import views as v

app_name = 'blog'
urlpatterns = [
        path('', v.PostLV.as_view(), name='index'),
        path('post/', v.PostLV.as_view(), name='post_list'),
        re_path(r'^post/(?P<slug>[-\w]+)/$',v.PostDV.as_view(), name='post_detail'),
        path('archive/', v.PostAV.as_view(), name='post_archive'),
        path('archive/<int:year>/', v.PostYAV.as_view(), name='post_year_archive'),
        path('archive/<int:year>/<str:month>/', v.PostMAV.as_view(), name='post_month_archive'),
        path('archive/<int:year>/<str:month>/<int:day>/', v.PostDAV.as_view(), name='post_day_archive'),
        path('archive/today/', v.PostTAV.as_view(), name='post_today_archive'),
        path('tag/', v.TagCloudTV.as_view(), name='tag_cloud'),
        path('tag/<str:tag>/', v.TaggedObjectLV.as_view(), name='tagged_object_list'),
        path('search/', v.SearchFormView.as_view(), name='search'),
        path('add/', v.PostCreateView.as_view(), name='add'),
        path('change/', v.PostChangeLV.as_view(), name='change'),
        path('<int:pk>/update/', v.PostUpdateView.as_view(), name='update'),
        path('<int:pk>/delete/', v.PostDeleteView.as_view(), name='delete'),
        ]

