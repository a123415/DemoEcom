from django.urls import path
from . import views

urlpatterns = [

    path('',views.Tasklistview.as_view(),name='home'),
    path('detail/<int:pk>/', views.TaskDetailview.as_view(), name='cbvdetail'),
    path('cupdate/<int:pk>/',views.TaskUpdateview.as_view(),name='cbvupdate'),
    path('cdelete/<int:pk>/',views.TaskDeleteview.as_view(),name='cbvdelete'),

]