from django.urls import path
from viewer import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('register', views.UserRegistrationView.as_view(), name='register'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('blog_detail/<int:id>', views.BlogDetailView.as_view(), name='blog_detail'),
    path('logout', views.UserLogoutView.as_view(), name='logout'),
    path('add_comment/<int:id>', views.AddComment.as_view(), name='comment'),
]  