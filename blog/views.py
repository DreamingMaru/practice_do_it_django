from django.views.generic import ListView, DeleteView
from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = '-pk'

class PostDetail(DeleteView):
    model = Post
    template_name = 'blog/post_detail.html'