from django import forms
from . models import Post


class PostForm(forms.ModelForm): # its a class, and its a form of type modelform,
	class Meta: # Class meta is a relationship that this form is for the model Post
		model = Post 
		fields = ['title' , 'content'] # now create a view to see this form
	