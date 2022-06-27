from django.conf import settings 
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
 
from .views import users_view, groups_view, update_view, home

urlpatterns = [ 
    path('users/', users_view, name="users"),
    path('', home, name="home"),
    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),
    path('savollar/', include('poll.urls', namespace='poll')),
    path('accounts/', include('userprofile.urls', namespace='userprofile')),
    path('news/', include('new.urls', namespace='new')),
    path('groups/', groups_view, name="groups"),
    
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

