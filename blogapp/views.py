from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,UpdateView,DeleteView,ListView,DetailView
from blogapp.task import *
from .models import *
from .forms import *
from django.urls import reverse_lazy
from blogapp.text_file_to_speech import *
from django.contrib import messages
from django.db.models import Q 
from bs4 import BeautifulSoup


class IndexView(View):
    def get(self, request):
        return render(request, 'blog-list.html')


class BlogDetailView(DetailView):
    model = Blog
    template_name='blog-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(slug=self.kwargs['slug'])
        return context

    

class AddBlogView(CreateView):
    model=Blog
    form_class=blogForm
    template_name='add-blog.html'    

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
            return render(self.request,'blog-list.html',{'form':form})
        else:
            return render(self.request,'login.html')

class UpdateBlogView(UpdateView):
    model = Blog
    template_name = "update.html"

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def LogoutView(request):
    logout(request)
    return redirect('/')


class DashboardBlogView(ListView):
    def get(self, request):
        data = Blog.objects.all()
        return render(request, 'dashboard.html', {'data': data})


def DeleteBlogView(request, id):
    obj = Blog.objects.get(id = id)
    print(obj)

    if request.method =="POST":
        a = obj.delete()
        print(a)
        return redirect("/")
    return redirect("/")
 

class ListBlogView(ListView):
    def get(self, request):
        blogsData = Blog.objects.all()
        return render(request, 'blog-list.html', {'blogsData': blogsData})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')



class LikeView(CreateView):
    model = Likes

    def post(self, request, *args, **kwargs):
        blog_id = request.POST.get('')

class SearchView(ListView):
    model = Blog
    template_name = 'search-result.html'
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context['object_list'])
        query = self.request.GET.get('q')

        if query:
            context['blogs'] = Blog.objects.filter(title__icontains=query)
            print(context)            
            tags = Tag.objects.filter(tag_name__contains=query)
            context['tags'] = tags
        return context
    

    # def get(self):
    #     search_result = []
    #     # print( self.request.GET.get('q'),"===================================")
    #     if self.request.method == 'GET':
    #         query = self.request.GET.get('q')
    #         print("----------------------------",query)
    #         if query:
    #             print("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")
    #             blogs = Blog.objects.all()
    #             print(blogs)
    #             # | Q(category__contains=query)
    #             # blogs = list(blogs_q)
    #             # tags = Tag.objects.filter(tag_name__contains=query)
    #             # a = [i.blog for i in tags]
    #             # search_result = a + blogs
    #             # print(tags,"--------------------------")
    #             # print(search_result,"@@--------------------------")

                
    #             return render(self.request, 'search-result.html', {'blogs':blogs})

    #         else:
    #             messages.success(self.request, 'not found')

