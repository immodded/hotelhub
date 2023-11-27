from django.urls import path
from .views import RoomListView, RoomDetailView, RoomCreateView

urlpatterns = [
    path('rooms/create/', RoomCreateView.as_view(), name="room_create"),
    path('rooms/', RoomListView.as_view(), name='room_list'),
    path('rooms/<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
]
