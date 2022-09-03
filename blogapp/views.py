# from django.shortcuts import render
# from django.views.generic import View

# # Create your views here.

# def home(request):
#    return render(request,'login.html')


# class IndexView(View):
#     def get(self, request):
#         return render(request, 'index.html')
from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    AllBlogs=Blog.objects.all()
    context={
        'blogs':AllBlogs,
    }
    print(AllBlogs)
    return render(request,'home.html',context)

def addBlog(request):
    form=blogForm()
    if request.method=='POST':
        print(request.POST, "======================", request.user)
        post_values = request.POST.copy()
        post_values['user.id']=request.user.id
        print(post_values, "000000000000000000000000000000000000000000000000")

        form=blogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form':form,
    }
    return render(request,'addblog.html',context)

# def likeBlog(request,pk):
#     blog=Tag.objects.get(id=pk)
#     blog.likes+=1
#     blog.save()
#     return redirect('/')