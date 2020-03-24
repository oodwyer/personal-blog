from django.shortcuts import render
from posts.models import blogPost
from markdown2 import Markdown

# Create your views here.
def splash(request):
	return render(request, "splash.html", {})

def blogPage(request):
    blogPosts = blogPost.objects.all()

    for x in blogPosts: 
        print(blogPost.name)

    return render(request, "blogPage.html", {"blogPosts": blogPosts})

def post(request, id): 
    post = blogPost.objects.get(id=id)
    content = post.content
    markdowner = Markdown()
    md = markdowner.convert(content)
    return render(request, "post.html", {"post": post, "content": md})

    


