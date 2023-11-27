from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from .models import Reservation
from django.views.generic import DetailView
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from room.models import Room
from guest.models import Guest

class CustomReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
        }

class Moddview(View):
    def get(self,request):
        return render(request,'modd.html')

class DashboardView(View):
    def get(self, request):
        total_rooms = Room.objects.all().count()
        total_guests = Guest.objects.all().count()
        total_reservations = Reservation.objects.all().count()
        context = {
            'total_rooms': total_rooms,
            'total_guests': total_guests,
            'total_reservations': total_reservations,
        }
        return render(request, 'dashboard.html', context)

class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    template_name = "form.html"
    form_class = CustomReservationForm

    def get_initial(self):
        initial = super().get_initial()
        guest_id = self.request.GET.get('guest_id')
        if guest_id:
            initial['guest'] = guest_id
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Reservation"
        return context

    def form_valid(self, form):
        room = form.cleaned_data['room']
        check_in_date = form.cleaned_data['check_in_date']
        check_out_date = form.cleaned_data['check_out_date']
        existing_reservations = Reservation.objects.filter(
            room=room,
            check_in_date__lt=check_out_date,
            check_out_date__gt=check_in_date
        )
        if existing_reservations.exists():
            form.add_error('room', 'This room is already booked for the selected dates.')
            return self.form_invalid(form)
        else:
            return super().form_valid(form)




class ReservationUpdateView(LoginRequiredMixin, UpdateView):
    model = Reservation
    template_name = "form.html"
    form_class = CustomReservationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Reservation"
        return context
    def form_valid(self, form):
        room = form.cleaned_data['room']
        check_in_date = form.cleaned_data['check_in_date']
        check_out_date = form.cleaned_data['check_out_date']
        existing_reservations = Reservation.objects.filter(
            room=room,
            check_in_date__lt=check_out_date,
            check_out_date__gt=check_in_date
        )
        if existing_reservations.exists():
            form.add_error('room', 'This room is already booked for the selected dates.')
            return self.form_invalid(form)
        else:
            return super().form_valid(form)    
    

class ReservationDetailView(LoginRequiredMixin, DetailView):
    model = Reservation
    template_name = "reservation_detail.html"

class ReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    paginate_by = 10
    context_object_name = "reservations"
    template_name = "reservation_list.html"
    def get_queryset(self):
        # Get the room number from the query parameters
        room_number = self.request.GET.get('room_number')

        # Filter reservations for the specified room number
        if room_number:
            return Reservation.objects.filter(room__room_number=int(room_number)).order_by('-id')
        else:
            return Reservation.objects.all().order_by('-id')
