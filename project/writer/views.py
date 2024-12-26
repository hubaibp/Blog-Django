from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from writer.forms import BlogWriteForm
from .models import BlogModel
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.
from django.contrib.auth import authenticate,login,logout



class BlogAdd(CreateView):
  template_name = 'add_blog.html'
  form_class = BlogWriteForm
  model = BlogModel
  success_url = reverse_lazy('blog_list')
  
  def form_valid(self,form):
    form.instance.user=self.request.user
    messages.success(self.request,"Blog Created")
    return super().form_valid(form)
  def form_invalid(self,form):
    messages.warning(self.request,"Invalid inputs")
    return redirect('login_view')
    
    
    
class  BlogList(ListView):
  template_name = 'blog_list.html'
  model = BlogModel
  context_object_name = 'blogslist' 
  
  def get_queryset(self):
    return BlogModel.objects.filter(user=self.request.user)
  
  
  
class BlogDelete(DeleteView):
    template_name = 'blog_delete.html'
    model = BlogModel
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('blog_list')

class BlogUpdate(UpdateView):
    model = BlogModel
    template_name = 'add_blog.html'
    form_class = BlogWriteForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('blog_list')
    
class UserLogoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,"Successfully logged out")
        return redirect('login')    