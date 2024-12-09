from django.urls import path
from . import views
urlpatterns = [
    # path('date/', views.current_datetime),
    path('',views.index,name='index'),
    # path('task/',views.task_list),
    # path('addtask/',views.add_task),

    # <!-- pass the name from the url -->
    path('delete/<str:name>',views.delete,name='delete'), 
    path('update/<str:name>',views.update,name='update')
]