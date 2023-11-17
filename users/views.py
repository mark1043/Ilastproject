from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView, FormView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordContextMixin, SetPasswordForm
from django.views import View
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import AbstractBaseUser
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from typing import Any

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    
    def get_queryset(self):
        return User.objects.get(id=self.request.user.id)

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        user = form.save()
        self.object = user
        return super().form_valid(form)

class SignUpSuccessView(TemplateView):
    template_name = 'signup_success.html'

class UserChangeView(LoginRequiredMixin, FormView):
    template_name = 'change.html'
    form_class = CustomUserChangeForm 
    success_url = reverse_lazy('users:profile')
    
    def form_valid(self, form):
        form.save()  
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'instance': self.request.user, 
        return kwargs

class PasswordResetConfirmView(PasswordContextMixin, FormView):
    post_reset_login: bool = True
    post_reset_login_backend: Any = 'django.contrib.auth.backends.ModelBackend'
    reset_url_token: str = 'token'
    title: Any = 'Password Reset Confirmation'
    form_class = SetPasswordForm
    token_generator: Any = default_token_generator
    validlink: bool = True
    user: Any = None
    
    def get_user(self, uidb64: str) -> AbstractBaseUser | None:
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        return user
