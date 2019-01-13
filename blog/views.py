from django.shortcuts import render
from .models import Post,Category

# Create your views here.

def list(request):
	category={'Category':Category.objects.all()}
	data= {'Posts':Post.objects.all().order_by("-date")}
	array={'data':data,'category':category}
	return render(request, 'blog/blog.html',array)

def post(request, id):
	category=Category.objects.all()
	post=Post.objects.get(id=id)
	return render(request,'blog/post.html',{'post':post,'Category':category})

def category(request):
	category={'Category':Category.objects.all()}
	return render(request,'blog/category.html',category)