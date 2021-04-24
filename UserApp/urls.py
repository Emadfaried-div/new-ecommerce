from django.urls import path
from .views import user_logout, user_login, user_register, user_update, user_password
from UserApp.views import usrprofiledata
app_name='UserApp'

urlpatterns = [
    path('logout/',user_logout, name='user_logout' ),
    path('login/',user_login, name='user_login' ),
    path('register/',user_register, name='user_register' ),
    path('userprofile/',usrprofiledata, name='userprofile' ),
    path('user_update/',user_update, name='user_update' ),
    path('password_update/',user_password, name='user_password' ),
]