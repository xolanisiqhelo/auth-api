from django.urls import path
from .views import RoleListView, RetrieveUserView, RoleDetailsView

urlpatterns = [
    path('role/', RoleListView.as_view()),
    path('RoleDetailsView/<pk>', RoleDetailsView.as_view()),
    path('role/<referenceNumber>/', RetrieveUserView.as_view())

]
