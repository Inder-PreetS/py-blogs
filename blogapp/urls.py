from django.urls import path, include
from .views import *
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [    
    path('', IndexView.as_view(),name='index'),
    path('add-blog/',AddBlog.as_view(),name='add-blog'),
    path('blog-detail/',BlogDetailView.as_view(),name='blog-detail'),
    # path('like/<str:pk>',likeBlog,name='like'),
    
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)