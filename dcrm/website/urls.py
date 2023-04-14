from django.urls import path
from .views import (
    home,
    logout_user,
    register_user,
    user_record,
    delete_user_record,
    add_user_record,
    update_user_record
) # login_user,

urlpatterns = [
    path("", home, name="home"),
    #path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("register/", register_user, name="register"),
    path("record/<int:pk>", user_record, name="record"),
    path('delete_record/<int:pk>', delete_user_record, name='delete_record'),
    path('add_record/', add_user_record, name='add_record'),
    path('update_record/<int:pk>', update_user_record, name='update_record'),
]
