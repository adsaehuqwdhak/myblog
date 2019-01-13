from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Category, Post
from django.template import loader
from django.http import HttpResponse, Http404
# Create your views here.
def index(request):
	category={'Category':Category.objects.all()}
	return render(request, 'pages/home.html',category)
def contact(request):
	category={'Category':Category.objects.all()}
	return render(request,'pages/contact.html',category)
def writes(request):
	category={'Category':Category.objects.all()}
	return render(request,'pages/writes.html',category)
def branch(request):
	category={'Category':Category.objects.all()}
	return render(request,'pages/branch.html',category)
def category(request):   
	category_list = Category.objects.order_by('-pub_date')[:5]
	template = loader.get_template('pages/category.html')
	context = {
	   'category_list': category_list,
	}
	return HttpResponse(template.render(context, request))
def detail(request,category_id):
	try:
		category_all=Category.objects.all()
		category = Category.objects.get(pk=category_id)
	except Category.DoesNotExist:
		raise Http404("Category does not exist")
	return render(request, 'pages/detail.html', {'category':category,'category_all':category_all})