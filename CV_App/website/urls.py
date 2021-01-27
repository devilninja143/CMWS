from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("Login", views.Login),
    path("CVView", views.CVView),
    path("register", views.registerUser),
    path("fullView/<str:pk>/", views.FullView, name="fullView"),
    path("Logout", views.Logout, name="Logout"),
    path("Edit", views.userChange, name="Edit"),
    path("password", views.passwordChange, name="password"),
    path("user", views.userPreview, name="user"),
    path("about", views.AboutPage, name="about")
]
