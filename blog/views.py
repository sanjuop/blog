from django.shortcuts import render
from blog.models import Post
# Create your views here.
def home(request):
    pub_posts = Post.objects.all()
    context = {"posts":pub_posts}
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {"title":"django_blog"})