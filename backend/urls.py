
from django.contrib import admin
from todo import views                            
from rest_framework import routers                    
from django.urls import path, include 
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

router = routers.DefaultRouter()                      
router.register(r'tasks', views.TodoView, 'task')     

# from django.urls import path  - DELETE THIS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))                
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''
This is the final step that completes the building of the API, we can now perform CRUD operations on the todo model
router allows us to do 2 things :
/todo/ -  this returns a list of all the Todo items (create and read operations can b done here)
/todos/id - this returns a single todo item using id primary key (update and delete operations ) 
'''
