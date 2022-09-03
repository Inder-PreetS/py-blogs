from re import L
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
# def AddBlog(request):
#     form=blogForm()
#     if request.method=='POST':
#         print(request.POST, "======================", request.user)
#         post_values = request.POST.copy()
#         post_values['user.id']=request.user.id
#         print(post_values, "000000000000000000000000000000000000000000000000")

#         form=blogForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context={
#         'form':form,
#     }
#     return render(request,'addblog.html',context)


