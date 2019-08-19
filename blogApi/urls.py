from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings

from blog.views import blog_list, home
from blog.api.views import BlogList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_list),
    path('home/', home),
    path('api/', BlogList.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
