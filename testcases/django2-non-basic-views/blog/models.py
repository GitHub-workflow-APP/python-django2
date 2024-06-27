from django.db import models
from django.urls import reverse
import logging

class Article(models.Model):
	title   = models.CharField(max_length=120) # Carries Taint.DB
	content = models.TextField() # Carries Taint.DB
	active  = models.BooleanField(default=True) # Doesn't carry Taint.DB

	logger = logging.getLogger(__name__)

	def get_absolute_url(self):
		self.logger.debug("Article:get_absolute_url " + self.title + "   " + self.content) # CWEID 117
		#return reverse("articles:article-detail", kwargs={"title": self.title})
		return reverse("articles:article-detail", kwargs={"title": 'title'})

	'''	
    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})
	'''
