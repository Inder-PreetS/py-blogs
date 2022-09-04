from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,UpdateView,DeleteView,ListView,DetailView
from blogapp.task import *
from .models import *
from .forms import *
from django.urls import reverse_lazy
from blogapp.text_file_to_speech import *
from django.urls import reverse


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class BlogDetailView(View):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog"] = Blog.objects.get(id=self.kwargs.get())
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
            given_tag = self.request.POST['tag']
            lis_tag = given_tag.split(",")
            form.save()
            for tag in lis_tag:
                Tag.objects.create(blog=form.instance, tag_name=tag)

            return render(self.request,'index.html',{'form':form})
        else:
            return render(self.request,'login.html')

class UpdateBlogView(UpdateView):
    model = Blog
    template_name = "update-blog.html"
    fields=['title', 'content', ]
    success_url=reverse_lazy('dashboard',)


def LogoutView(request):
    logout(request)
    return redirect('/')


class DashboardBlogView(ListView):
    def get(self, request):
        if self.request.user.is_authenticated:
            data = Blog.objects.filter(user = self.request.user)
            return render(request, 'dashboard.html', {'data': data})


class Dashboard(ListView):
    def get(self, request):
        data = Blog.objects.all()
        return render(request, 'dashboard.html', {'data': data})


# class UpdateBlogView(UpdateView):
#     def get(self, request):
#         return render(request, 'edit-blog.html')


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
        data = Blog.objects.all()
        return render(request, 'post-list.html', {'data': data})

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

