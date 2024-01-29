# from django.contrib import admin
# from django.db import router
# from django.urls import path, include
# # from crud.views import  CommentViewsets
# # from rest_framework import routers


# # router = routers.DefaultRouter()
# # router.register(r'comment', CommentViewsets)



# urlpatterns = [

#         path('',include(router.urls)), 
#     path('api/crud/home/',views.home.as_view,name="home"),
#     path('api/crud/add-adoption/',views.add_adoption.as_view(),name="add"),
#     path('api/crud/delete-dashboard/<int:name>',views.delete_dashboard.as_view(),name="delete"),
#     path('api/crud/update-dashboard/<int:name>',views.update_dashboard.as_view(),name="update"),
#     path('api/crud/do-update-dashboard/<int:name>',views.do_update_dashboard.as_view()),
   
#  ]