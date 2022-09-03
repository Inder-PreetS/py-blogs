from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.views.generic import View,CreateView
from blogapp.task import *
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
    

    def form_valid(self,form):
        if self.request.user.is_authenticated:
            form.instance.user=self.request.user
            form.instance.audio_status='Processing'
            form.instance.state = get_ip()
            form.save()
            return render(self.request,'index.html',{'form':form})
        else:
            return redirect('login')
            # return render(self.request,'login.html')

    

    
    

# logout 
def LogoutView(request):
    logout(request)
    return redirect('/')

