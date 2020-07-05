from django.urls import path
from .views import RoleListView, RetrieveUserView

urlpatterns = [
    path('role/', RoleListView.as_view()),
    path('role/<referenceNumber>/', RetrieveUserView.as_view())
]