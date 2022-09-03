from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('blog_detail/',BlogDetailView.as_view(),name='blog_detail'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)