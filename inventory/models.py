from django.db import models

# Create your models here.
from django.db import models


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	product_name = models.CharField(max_length=100)
	buying_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	profit = models.DecimalField(max_digits=10, decimal_places=2,default=0)

	def __str__(self):
		return f"{self.product_name}"
	

class Client(models.Model):	
		created_at = models.DateTimeField(auto_now_add=True)
		client_name = models.CharField(max_length=200,default="client")
		paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
		remaining = models.DecimalField(max_digits=10, decimal_places=2, default=0)
		credit_deposit= models.CharField(max_length=50)

		def __str__ (self):
			return f"{self.client_name}"
		



	

