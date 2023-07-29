
from django.urls import path
from block.views import render_post , post_detail

app_name = 'blog'

urlpatterns = [

    path('', render_post, name="home_post"),
    path('<int:post_id>',  post_detail , name="post_detail")
    
] 