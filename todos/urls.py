from django.urls import path, include
from todos import views
from django.contrib import admin

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>/',views.detail,name='detail'),
    path('insert/',views.insert,name='insert'),
    path('db_insert/',views.db_insert,name='db_insert'),
    path('<int:id>/delete/',views.delete,name='delete'),
    path('<int:id>/db_update/',views.db_update,name='db_update'),
    path('<int:id>/update/',views.update,name='update'),
    # path('<int:id>/',views.notnull,name='detail'),
]