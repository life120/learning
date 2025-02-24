from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name='accounts'

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path('token/new/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('sample/public/', PublicView.as_view(), name='public-view'),
    path('sample/protected/', ProtectedView.as_view(), name='protected-view'),
]
