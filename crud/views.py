
from multiprocessing import context
from urllib import request

from django.shortcuts import render,redirect
from django.views import View
from crud.models import Comment
from rest_framework import viewsets
from crud.serializers import CommentSerializer
# from rest_framework.decorators import action
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import AllowAny



class CommentViewsets(viewsets.ModelViewSet):
   queryset = Comment.objects.all()
   serializer_class = CommentSerializer
   # authentication_classes = [SessionAuthentication]
   # permission_classes = [AllowAny]


   # Exploring Decoration

   # @action(detail=True, methods=['get'])
   # def users(self,request,pk=None):
   #    try:
   #       Comment = Comment.objects.get(pk=pk)
   #       users = users.objects.filter(Comment=Comment)
   #       users_serializer = UsersSerializer(users, many = True, context={'request':request})

   #       return Response(users_serializer.data)
   #    except Exception as e:
   #       print (e)
   #       return Response({
   #          'message' : 'User might not exist'
   #       })



# class home(viewsets.ModelViewSet):
#     def get(self, request):
#         return render(request, 'dashboard\home.html')






# class add_adoption(views):
#    def post (self, request):
    
#     dashboard_email =  request.POST.get("dashboard_email")
#     dashboard_title =  request.POST.get("dashboard_title")
#     dashboard_description = request.POST.get("dashboard_description")
#     dashboard_image = request.POST.get("dashboard_image")
    

#     s = Comment()
#     s.email = dashboard_email
#     s.title = dashboard_title
#     s.description = dashboard_description
#     s.image = dashboard_image
    
#     s.save()
#     return redirect("home")
   
#    def get(self,request): 
#     return render(request, 'dashboard/add_adoption.html')
   
   


# class delete_dashboard(views):
#    def get(self, request, name): 
#     s=Comment.objects.get(pk=name)
#     s.delete()
#     return redirect("/dashboard/home/")
  
  
# class update_dashboard(views):
#    def get(self, request, name):
#       dashboard=Comment.objects.get(pk=name)
#       context = "{'dashboard/home':dashboard}"
#       return render(request,"dashboard/update_adoption.html", context)


# class do_update_dashboard(views):
#     def post(self, request,name):
#        dashboard_email =  request.POST.get("dashboard_email")
#        dashboard_title =  request.POST.get("dashboard_title")
#        dashboard_description = request.POST.get("dashboard_description")
#        dashboard_image = request.POST.get("dashboard_image")

    
#        dashboard=Comment.objects.get(pk=name)
#        dashboard.email = dashboard_email
#        dashboard.title = dashboard_title
#        dashboard.description = dashboard_description
#        dashboard.image = dashboard_image
       
#        dashboard.save()
       
#        return redirect("/dashboard/home/")

