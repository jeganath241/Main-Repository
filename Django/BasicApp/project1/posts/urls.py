from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView

urlpatterns = [
    # path("myapp/", views.index, name="myapp"),
    path('posts/', HomeView.as_view(), name="posts")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)