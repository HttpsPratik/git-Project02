from django.urls import path
from crud.views import ListView,DetailView



urlpatterns = [
  
    path('list/', ListView.as_view(), name='ListView'),   
    path('detail/<int:pk>/', DetailView.as_view(), name='DetailView'),
    
 
]
