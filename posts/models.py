# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Post( models.Model):
	content = models.CharField(max_length=255)
	title = models.TextField()
	updated = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.title
