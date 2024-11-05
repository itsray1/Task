from django.urls import path
from . import views


#api/tasks/
urlpatterns=[
    path('<int:pk>/update/',views.TaskUpdateAPIView.as_view()),
    path('<int:pk>/delete/',views.TaskDeleteAPIView.as_view()),
    path('<int:pk>/',views.TaskDetailAPIView.as_view()),
     path('',views.Task_Listcreate_view),
  

]
