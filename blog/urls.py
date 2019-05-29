from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
        path('' ,views.index ,name='index'),
        path('portfolio/' ,views.work ,name='portfolio'),
        path('profile/' ,views.profile ,name='profile'),
        path('contact/' ,views.contact ,name='contact'),
        path('blog/' ,views.blog ,name='blog')
]
