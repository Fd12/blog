# -*- coding: utf-8 -*-
from django.http import HttpResponse
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_home(request):
	return HttpResponse('<h1>hello</h1>')

def post_create(request):
	return render(request, 'post_create.html', {})


def post_list(request):  # its a function that takes a request
	objects = Post.objects.all() #we created a new variable called objects that means all objects in the POST

	context = {
 	"post_items": objects,

	}
	return render(request, "list.html", context)



def post_detail(request):
	item = Post.objects.get(id=1) #item is just a name of variable, get only 1 item) (Post- its a model)
	context = {
		"item" : item,
	}
	return render(request, "detail.html", context)



# Item or Display error 404, 
#def post_detail(request):
#	item = get_object_or_404(Post,id=1) #item is just a name of variable, get only 1 item) (Post- its a model)
#	context = {
#		"item" : item,
#	}
# 	return render(request, "detail.html", context)



#def post_detail(request, post_id): //same as the line below (post_id)
#item = get_object_or_404(post, id=post_id) // same as the line above (post_id)
# context = {
	#"item":item,
	#}
	#return render (request, "detail.html", context)
