from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import CreateView,ListView
from .models import Room
from .forms import BookingForm
from django.urls import reverse_lazy
from main.models import Reservation
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

class RoomCreateView(LoginRequiredMixin, CreateView):
    model = Room
    template_name = "form.html"
    fields = "__all__"
    success_url = reverse_lazy('room_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Create Room'
        return context
    

class RoomListView(LoginRequiredMixin, ListView):
    model = Room
    context_object_name = "rooms"
    paginate_by = 10
    template_name = "room_list.html"

class RoomDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        room = get_object_or_404(Room, pk=pk)
        current_datetime = timezone.now()
        reservations = room.reservation_set.filter(check_in_date__gte=current_datetime.date()).order_by('check_in_date')
        return render(request, 'room_detail.html', {'room': room, 'reservations': reservations,})

