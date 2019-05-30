from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
        path('' ,views.index ,name='index'),
        path('work/' ,views.work ,name='work'),
        path('profile/' ,views.profile ,name='profile'),
        path('blog/' ,views.blog ,name='blog')
]
