from django.urls import path
from .views import GuestListView, GuestDetailView, GuestCreateView

urlpatterns = [
    path('guests/create/', GuestCreateView.as_view(), name="guest_create"),
    path('guests/', GuestListView.as_view(), name='guest_list'),
    path('guests/<int:pk>/', GuestDetailView.as_view(), name='guest_detail'),
    # Add other URLs as needed
]
