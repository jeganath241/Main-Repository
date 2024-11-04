from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
from .form import CustomUserCreationForm


# import logging
# from django.contrib.auth.views import PasswordResetView

# logger = logging.getLogger(__name__)

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "signup.html"



# class CustomPasswordResetView(PasswordResetView):
#     template_name = 'registration/password_reset_form.html'
    
#     def get(self, request, *args, **kwargs):
#         logger.debug(f"Using template: {self.template_name}")
#         return super().get(request, *args, **kwargs)
