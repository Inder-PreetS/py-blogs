from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *
from .forms import *


# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class BlogDetailView(View):
    def get(self, request):
        return render(request, 'post-details.html')


class AddBlogView(View):
    def get(self, request):
        form = blogForm()
        return render(request, 'add-blog.html', {'form': form})

    def post(self,form):
        print(form, 'form')
        print(self.request.user,'1111111111111111111111111111111111111111111')
        if self.request.user.is_authenticated:
            print(self.request)
            print(self.request.user)
            form.instance.user=self.request.user
            form.save()
            return render(self.request,'index.html',{'form':form})
        else:
            print('not authenticated==================wqsax')
            return render(self.request,'login.html')

# logout 
def LogoutView(request):
    logout(request)
    return redirect('/')

