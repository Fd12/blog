# -*- coding: utf-8 -*-
from django.http import HttpResponse
from .models import Post
from django.shortcuts import render, get_object_or_404 , redirect
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import Http404


# Create your views here.
def post_home(request):
	return HttpResponse('<h1>hello</h1>')



def post_list(request):  # its a function that takes a request
	objects = Post.objects.all() #we created a new variable called objects that means all objects in the POST
	paginator = Paginator(objects, 5) # Show 25 contacts per page

	number = request.GET.get('page')
	try:
		objects = paginator.page(number)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		objects = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		objects = paginator.page(paginator.num_pages)

	context = {
	"post_items": objects,
	"title": "title",
	"user": request.user,
	}
	return render(request, "post_list.html", context)



def post_detail(request, post_id):
	item = get_object_or_404(Post, id=post_id) #item is just a name of variable, get only 1 item) (Post- its a model)
	context = {
		"item" : item,
		
	}
	return render(request, "detail.html", context)





#item = get_object_or_404(post, id=post_id) // same as the line above (post_id)
# context = {
	#"item":item,
	#}
	#return render (request, "detail.html", context)


def post_create(request, post_id=id ):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	form = PostForm(request.POST or None)

	if form.is_valid():
		form.save()
		messages.success(request, "Awesome, You just added a Blog Post")
		return redirect('posts:post_list')
	context = {
		 # we create a postform object called form PostForm is the name of the model
		"form" : form
	}
	return render (request, 'post_create.html' , context)










#function about How to edit a form, 
def post_update(request, post_id):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	item = Post.object.get(id=post_id)

	form = PostForm(request.POST or None, instance=item) #it always has to be instance
	if form.is_valid():
		form.save
		messages.info(request, "Hey, You just changed a Blog Post")
		return redirect("posts:list")
	context = {
		 # we create a postform object called form PostForm is the name of the model
		"form" : form,
		"item" : item,
	}
	return render (request, 'post_create.html' , context)




#Delete a Post 

def post_delete(request, post_id):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	Post.object.Get(id=post_id).delete()
	messages.warning(request, "Oops , You just added a Blog Post")
	return redirect ("more:list")







