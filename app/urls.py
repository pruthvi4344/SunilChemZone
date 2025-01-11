from django.urls import path, include
from app import views
from django.shortcuts import render
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup', views.user_signup, name='signup'),
    path('logout', views.user_logout, name='logout'),
    path('verification/', lambda request: render(request, 'account/verification_sent.html'), name='verification'),
    path('get-chapters/', views.get_chapters, name='get_chapters'),
    path('post/<int:id>/', views.blog, name='blog'),
    # path('post/<int:id>', views.post,)
    # path('filter-materials/', views.filter_materials, name='filter_materials'),
    # path('verification_sent', views.verification, name='verification')
    # path('accounts/', include('allauth.urls')),
]














# study , study