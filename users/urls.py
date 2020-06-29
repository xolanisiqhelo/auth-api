from django.urls import path
from .views import SignUpView,LogInView, LogOutView

urlpatterns = [
    path('user/sign_up/', SignUpView.as_view(), name='sign_up'),
    path('user/sign_in/', LogInView.as_view(), name='sign_in'),  # new
    path('user/sign_out/', LogOutView.as_view(), name='sign_out'),  # new
]
