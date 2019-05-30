from django.urls import path

from . import views

app_name = 'blogKr'
urlpatterns = [
        path('' ,views.indexKr ,name='indexKr'),
        path('work/' ,views.workKr ,name='workKr'),
        path('profile/' ,views.profileKr ,name='profileKr'),
        path('blog/' ,views.blogKr ,name='blogKr')
]
