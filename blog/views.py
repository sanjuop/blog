from django.shortcuts import render

pub_posts = [
            {"title":"Blog Post 1",
            "author":"Sanjay",
            "content":"This is my first post",
            "published_on":"20 nov 2020"},
            {"title":"Blog Post 2",
            "author":"Nivedita",
            "content":"This is my second post",
            "published_on":"21 nov 2020"}
            ]

# Create your views here.
def home(request):
    context = {"posts":pub_posts}
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {"title":"django_blog"})