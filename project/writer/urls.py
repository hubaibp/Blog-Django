from django.urls import path
from . import views

urlpatterns = [
    path('write', views.BlogAdd.as_view(), name='write'),
    path('blog_list', views.BlogList.as_view(), name='blog_list'),
    path('blog_delete/<int:id>', views.BlogDelete.as_view(), name='blog_delete'),
    path('blog_update/<int:id>', views.BlogUpdate.as_view(), name='blog_update'),
    path('logout', views.UserLogoutView.as_view(), name='logout'),
]