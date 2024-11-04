from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import HomePageView, AboutPageView

urlpatterns = [
    # path("myapp/", views.index, name="myapp"),
    path('myapp/', HomePageView.as_view(), name="myapp"),
    path('about/', AboutPageView.as_view(), name="about")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)