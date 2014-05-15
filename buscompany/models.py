from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Staff(models.Model):
	tck_no = models.CharField(max_length=11,primary_key=True)
	name = models.CharField(max_length=50)
	salary = models.DecimalField(max_digits=7, decimal_places=2)
	phone = models.CharField(max_length=18)
	home_address = models.CharField(max_length=100)
	start_date = models.CharField(max_length=10)
	class Meta:
		db_table = 'Staff'

class SystemUser(models.Model):
	tck_no = models.ForeignKey(Staff,primary_key=True,db_column='tck_no')
	user = models.OneToOneField(User)
	class Meta:
		db_table = 'SystemUser'

class Manager(models.Model):
	tck_no = models.ForeignKey(SystemUser,primary_key=True,db_column='tck_no')
	position = models.CharField(max_length=40)
	class Meta:
		db_table = 'Manager'

class SalesOffice(models.Model):
	city = models.CharField(max_length=20)
	address = models.CharField(max_length=100)
	phone = models.CharField(max_length=18)
	class Meta:
		db_table = 'SalesOffice'
		
class Salesperson(models.Model):
	tck_no = models.ForeignKey(SystemUser,primary_key=True,db_column='tck_no')
	office_id = models.ForeignKey(SalesOffice,db_column='office_id')
	tickets_sold = models.PositiveIntegerField()
	class Meta:
		db_table = 'Salesperson'

		