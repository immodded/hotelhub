from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserChangeForm

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'form.html'
    success_url = reverse_lazy('profile')
    fields = ['first_name','last_name','email',]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Profile Update"
        return context
    
    def get_object(self):
        return self.request.user


class PasswordUpdateView(LoginRequiredMixin , PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'form.html'
    success_url = reverse_lazy('index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Password change"
        return context
    

@login_required
def ProfileView(request):
    return render(request, 'accounts/profile.html')