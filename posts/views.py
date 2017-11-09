# -*- coding: utf-8 -*-
from django.http import HttpResponse
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.contrib import messages


# Create your views here.
def post_home(request):
	return HttpResponse('<h1>hello</h1>')

def post_create(request):
	return render(request, 'post_create.html', {})


def post_list(request):  # its a function that takes a request
	objects = Post.objects.all() #we created a new variable called objects that means all objects in the POST

	context = {
 	"post_items": objects,
 	"title": "title",
 	"user": request.user,

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


def post_create(request, post_id):
	form = PostForm(request.POST or None)

	if form.is_valid():
		form.save()
		messages.success(request, "Awesome, You just added a Blog Post")
		return redirect('more:list')
	context = {
		 # we create a postform object called form PostForm is the name of the model
		"form" : form
	}
	return render (request, 'post_create.html' , context)










#function about How to edit a form, 
def post_update(request, post_id):
	item = Post.object.get(id=post_id)

	form = PostForm(request.POST or None, instance=item) #it always has to be instance
	if form.is_valid():
		form.save
		messages.info(request, "Hey, You just changed a Blog Post")
		return redirect("more:list")
	context = {
		 # we create a postform object called form PostForm is the name of the model
		"form" : form,
		"item" : item,
	}
	return render (request, 'post_create.html' , context)




#Delete a Post 

def post_delete(request, post_id):
	Post.object.Get(id=post_id).delete()
	messages.warning(request, "Oops , You just added a Blog Post")
	return redirect ("more:list")







