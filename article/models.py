from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=80)
	body = models.TextField()
	likes = models.IntegerField(default=0)

	def _unicode_(self):
		return self.title

	def __str__(self):
		return self.title

class Comment(models.Model):
	article = models.ForeignKey(Article)
	text = models.TextField(254)

	def _unicode_(self):
		return self.text