from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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
    form_class = CustomUserChangeForm  # Use your custom form for user changes
    success_url = reverse_lazy('users:profile')
    
    def form_valid(self, form):
        form.save()  # You don't need the update method if you're using a ModelForm
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'instance': self.request.user,  # Pass the user instance to populate the form
        })
        return kwargs