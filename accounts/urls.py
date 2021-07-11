from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('login/',views.login_view,name='login'),
    # login
    path('logout',views.logout_view,name='logout'),
    # logout
    path('signup/',views.signup_view,name='signup')
    # registration / signup
]