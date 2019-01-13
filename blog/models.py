from django.db import models

# Create your models here.
class Category(models.Model):
	category_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField('date published',null=True)
	def __str__(self):
		return self.category_text
class Post(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	title=models.CharField(max_length=100)
	body=models.TextField()
	date=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title 
