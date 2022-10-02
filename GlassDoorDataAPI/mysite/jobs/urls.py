from django.urls import path 
from . import views
app_name= 'jobs'

urlpatterns=[
    path('list/', views.listjobs ,name = 'list_view'),
    path('info/' ,views.infoview, name ='info'),
]