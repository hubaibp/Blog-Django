from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import UserRegistrationForm,UserLoginForm,AddCommentForm
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate,login,logout
from writer.models import BlogModel
from .models import CommentModel

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs1'] = BlogModel.objects.all()
        return context
    
    
class UserRegistrationView(CreateView):
    template_name = 'register.html'
    form_class = UserRegistrationForm
    
    def form_valid(self,form):
        User.objects.create_user(**form.cleaned_data)
        messages.success(self.request,"User Created")
        return redirect('login')
    def form_invalid(self,form):
        messages.warning(self.request,"Invalid inputs")
        return redirect('register')
    
class UserLoginView(View):
    def get(self,request):
        form=UserLoginForm()
        return render(request,'login.html',{'form':form})
    def post(self,request):
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        utype = request.POST.get('usertype')
        user = authenticate(request,username=uname,password=pwd,)    
        if user:
            login(request,user)
            messages.success(request,"Login Success")
            if utype == 'viewer':
                return redirect('home')
            else:
                return redirect('blog_list')
        else:
            messages.warning(request,"Invalid Credentials")
            return redirect('login')
        
class UserLogoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,"Logout Success")
        return redirect('login')
    
class BlogDetailView(TemplateView):
    template_name = 'blog_detail.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogy'] = BlogModel.objects.get(id=self.kwargs.get('id'))
        return context
    
    
# class AddCommentView(TemplateView):
#     template_name = 'comment.html'
    
#     def get(self,request,id):
#         form = AddCommentForm()
#         return render(request,self.template_name,{'form':form})
    
     
# class AddComment(View):
#     def get(self,request,*args,**kwargs):
#         form = AddCommentForm()
#         return render(request,"add_comment.html",{"form":form})
#     def post(self,request,*args,**kwargs):
#         blog = BlogModel.objects.get(id=kwargs.get("id"))
#         user = request.user
#         form = AddCommentForm(request.POST)
#         if form.is_valid():
#             CommentModel.objects.create(blog = blog,user = user,**form.cleaned_data)
#             messages.success(request,'Comment added')
#             return redirect("home_view")

class AddComment(TemplateView):
    template_name = "comment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = get_object_or_404(BlogModel, id=kwargs.get("id"))
        context["form"] = AddCommentForm()
        context["blog"] = blog  # Pass the blog object to the template
        context["comments"] = CommentModel.objects.filter(blog=blog)  # Pass comments for the blog
        return context

    def post(self, request, *args, **kwargs):
        blog = get_object_or_404(BlogModel, id=kwargs.get("id"))
        form = AddCommentForm(request.POST)
        if form.is_valid():
            CommentModel.objects.create(blog=blog, user=request.user, **form.cleaned_data)
            messages.success(request, 'Comment added')
            return redirect("blog_detail",id=blog.id)
        
        else:
            # If the form is invalid, re-render the page with errors
            context = self.get_context_data(**kwargs)
            context["form"] = form
            return self.render_to_response(context)