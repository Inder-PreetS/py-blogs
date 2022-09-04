from django.urls import path, include
from .views import *
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [    
    path('', IndexView.as_view(),name='index'),
    path('add-blog/',AddBlogView.as_view(),name='add-blog'),
    path('blog-detail/',BlogDetailView.as_view(),name='blog-detail'),
    path('logout/',LogoutView,name='logout'),
    path('all-blogs/',ListBlogView.as_view(),name='all-blogs'),

    path('dashboard/',views.DashboardBlogView.as_view(),name='dashboard'),
    path('edit-blog/<int:id>/',views.UpdateBlogView.as_view(),name='edit-blog'),
    path('delete-blog/<int:id>/',views.DeleteBlogView,name='delete-blog'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('search/', views.SearchView.as_view(),name = 'search')
    # path('like/<str:pk>',likeBlog,name='like'),
    
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)