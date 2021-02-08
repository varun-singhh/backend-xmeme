from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview,name="api-overview"),
    path('memes/',views.taskList,name="memes-list"),
    path('memes-detail/<str:pk>/',views.taskDetail,name="memes-detail"),
    path('memes-create/',views.taskCreate,name="memes-create"),
    path('memes-update/<str:pk>/',views.taskUpdate,name="memes-update"),
    path('memes-delete/<str:pk>/',views.taskDelete,name="memes-delete"),
]



