from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from dashboards import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('register/', accounts_views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]