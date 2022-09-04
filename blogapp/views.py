from re import L
from typing import Generic
from urllib import request
from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,UpdateView,DeleteView,ListView,DetailView
from blogapp.task import *
from .models import *
from .forms import *
from blogapp.text_file_to_speech import *


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
class AddBlog(CreateView):
    model=Blog
    form_class=blogForm
    template_name='add-blog.html'
    # success_url='/'

    # def getContent():
    #     soup = BeautifulSoup(html)
    #     print (soup.text)
    

    def form_valid(self,form):
        if self.request.user.is_authenticated:
            form.instance.user=self.request.user
            form.instance.audio_status='Processing'
            form.instance.state = get_ip()
            html = form.instance.content
            soup = BeautifulSoup(html)
            form.instance.audio_url = text_to_audio("Title is "+form.instance.title+"."+ "Description is"+soup.text, form.instance.title)
            # for tag in form.instance.tag_name:
            #     Tag.objects.create(blog=form.instance, tag_name=tag)

            form.save()
            return render(self.request,'index.html',{'form':form})
        else:
            return render(self.request,'login.html')

# class ModelUpdateView(UpdateView):
#     model = Blog
#     template_name = "update.html"

#     def put(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         print(self.object,'======================')
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
        # return self.post(request, *args, **kwargs)


    

    
    


