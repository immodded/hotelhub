from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Guest
from django.views.generic import CreateView,ListView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class GuestCreateView(LoginRequiredMixin, CreateView):
    model = Guest
    template_name = "form.html"
    fields = "__all__"
    success_url = reverse_lazy('room_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Guest"
        return context
    

class GuestListView(LoginRequiredMixin, ListView):
    model = Guest
    context_object_name = "guests"
    paginate_by = 10
    template_name = "guest_list.html"
    def get_queryset(self):
        return Guest.objects.all().order_by('-id')

class GuestDetailView(LoginRequiredMixin, DetailView):
    model = Guest
    template_name = "guest_detail.html"
    context_object_name = "guest"

