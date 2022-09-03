from django.urls import path, include
from .views import *
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home),
    
    path('', home,name='home'),
    path('add/',addBlog,name='addblog'),
    # path('like/<str:pk>',likeBlog,name='like'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)