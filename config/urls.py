from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path('users/', include('users.urls', namespace='users')),
                  path('', include('newsletter.urls', namespace='newsletter')),
                  path('blog/', include('blog.urls', namespace='blog')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
