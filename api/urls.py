from django.urls import path
from .views import RoleDetailsView, RoleListView,RetrieveUserView

urlpatterns = [
    path('role/', RoleListView.as_view()),
    # path('role/<student_no>/', RoleDetailsView.as_view()),
    path('role/<student_no>/', RetrieveUserView.as_view())
]