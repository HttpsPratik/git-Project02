from django.urls import path
from crud.views import CrudDetailView, CrudListView

urlpatterns = [
    path('list/', CrudListView.as_view(), name='ListView'),   
    path('detail/<int:pk>/', CrudDetailView.as_view(), name='DetailView'),]
