from django.urls import path

from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path('blog/', BlogListView.as_view(), name = "blog"),
    path('blog/details/<int:pk>', BlogDetailView.as_view(), name = "post_details"),
    path('blog/details/new', BlogCreateView.as_view(), name = "post_new"),
    path('blog/details/<int:pk>/edit', BlogUpdateView.as_view(), name="post_edit"),
    path('blog/details/<int:pk>/delete', BlogDeleteView.as_view(), name="post_delete"),
    # path('logout/', LogoutView.as_view(), name="logout"),
    # path('login/', LoginView.as_view(), name="login")
]