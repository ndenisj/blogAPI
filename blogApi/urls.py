from django.contrib import admin
from django.urls import path

from blog.views import blog_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_list)
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
