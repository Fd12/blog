# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.template.defaultfilters import slugify

class Post( models.Model):
	content = models.CharField(max_length=40)
	#slug = models.SlugField(unique=True)
	title = models.TextField()
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


def __str__(self):
	return self.title


def get_absolute_url(self):
	return reverse("post:detail", kwarges={"post_id": self.id})

class Meta:
	ordering = ['title']



#def pre_save_post_function(sender, instance, *args, **kwarges):
#args going to suggest values as list, kwargs are like dictionery,
#both args and kwarges values are like: ignore args and kwarges( everything in argument and keyword arguments ingore)
#sender: is going to be a argument
#instance: will be key to the arguments.

	
#re_save.connect(pre_save_post_function, sender=Post)
#	print (args)
#	print (kwargs)
#trigger this funciton by creating or updating a funciton
#some function will be checking the value of the title, if no slug then it will apply the slug
# it orders the posts by the name 