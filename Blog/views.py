from django.shortcuts import render
from Blog.models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()

    return render(request, template_name="index.html", context={"posts":posts})

