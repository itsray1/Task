from django.shortcuts import render
from rest_framework import generics, permissions,authentication
from .models import Task
from .serializers import TaskSerializer

#################Create####################

class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    authentication_classes=[authentication.SessionAuthentication]
    permission_classes=[permissions.IsAdminUser,permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
         serializer.save(user=self.request.user)
      

    def get_queryset(self,*args,**kwargs):
        qs=super().get_queryset(*args,**kwargs) 
        request=self.request
        user=request.user
        if not user.is_authenticated:
            return Task.objects.none()
        #print(request.user)
        return qs.filter(user=request.user)   


Task_Listcreate_view=TaskListCreateAPIView.as_view()


#################Detail####################

class TaskDetailAPIView(generics.RetrieveAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer

##################Update###################

class TaskUpdateAPIView(generics.UpdateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    lookup_field='pk'

    def perform_update(self, serializer):
       serializer.save()
       

###################Delete##################   

class TaskDeleteAPIView(generics.DestroyAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    lookup_field='pk'

    def perform_Delete(self, instance):
       super().perform_destroy(instance)
