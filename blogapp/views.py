from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView
from blogapp.task import *
from .models import *
from .forms import *


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class BlogDetailView(View):
    def get(self, request):
        return render(request, 'post-details.html')


class AddBlogView(CreateView):
    model=Blog
    form_class=blogForm
    template_name='add-blog.html'    

    def form_valid(self,form):
        if self.request.user.is_authenticated:
            form.instance.user=self.request.user
            form.instance.audio_status='Processing'
            form.instance.state = get_ip()
            form.save()
            return render(self.request,'index.html',{'form':form})
        else:
            return redirect('accounts/google/login/?process=login')    
    
 
def LogoutView(request):
    logout(request)
    return redirect('/')


class ListBlogView(ListView):
    def get(self, request):
        data = Blog.objects.all()
        return render(request, 'dashboard.html', {'data': data})


class UpdateBlogView(UpdateView):
    def get(self, request):
        return render(request, 'edit-blog.html')


def DeleteBlogView(request, id):
    context ={}
    obj = Blog.objects.get(id = id)

    if request.method =="POST":
        obj.delete()
        return redirect("/")
 
    return render(request, "delete_view.html", context)