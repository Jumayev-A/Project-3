from django.urls import path
from my_app import views
app_name='my_app'
urlpatterns = [
    path('', views.home, name="home"),
    path('create_category/', views.create_category, name='create_category'),
    path('del-category/<int:pk>/', views.del_category, name='delete_category'),
    path('update-category/<int:pk>/', views.update_category, name='update_category'),
    path('blogs/<int:pk>', views.view_blog, name='blog_list'),
    path('create_blog/<int:pk>/', views.create_blog, name='create_blog'),
    path('del-blog/<int:pk>/', views.del_blog, name='delete_blog'),
    path('update-blog/<int:pk>/', views.update_blog, name='update_blog'),
    path('detail_blog/<int:id>/', views.blog_detail, name='detail_blog'),
]
