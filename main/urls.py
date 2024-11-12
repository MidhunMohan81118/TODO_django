from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home_page"),
    path("task/<int:id>",views.task,name="Tasks"),
    path("task_list/",views.list_tasks,name="Task_list"),
    path("createtask/",views.create_task,name="create_task"),
]
