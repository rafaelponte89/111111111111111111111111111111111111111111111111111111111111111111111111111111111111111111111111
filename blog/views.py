from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Blog

def list_blogs(request):
    blogs = Blog.objects.all()
    return render(request, "blog/list.html",{"blogs":blogs})
    
def detail_blog(request,pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, "blog/detail.html",{"blog":blog})