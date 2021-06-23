
from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('' ,blog_view,name='index'),
    path('<int:pid>' ,blog_single,name='single'),
    path('test',test,name='test'),
]
