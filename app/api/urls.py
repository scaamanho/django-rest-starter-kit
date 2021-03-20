from django.urls import include, path
from . import views

# existing serializer, viewset, router registrations code
urlpatterns = [ 
    path('todos', views.TodoList.as_view(), name='index'),
    #path('todos', views.todo_list, name='index'),
    path('todos/<pk>', views.TodoDetail.as_view(), name='index'),
    path('custom', views.TodoCustomView.as_view(), name='index'),
    path('completed', views.TodoCustomCompleted.as_view(), name='index'),
    #path('todos_completed', views.todo_list_completed, name='index'),
]
