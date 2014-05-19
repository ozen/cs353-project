from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
	tck_no = models.CharField(max_length=11,primary_key=True)
	name = models.CharField(max_length=50,db_index=False)
	salary = models.DecimalField(max_digits=7, decimal_places=2,db_index=False)
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
		unique_together = (('city','address'),)

class Salesperson(models.Model):
	tck_no = models.ForeignKey(SystemUser,primary_key=True,db_column='tck_no')
	office_id = models.ForeignKey(SalesOffice,db_column='office_id',db_index=True)
	tickets_sold = models.PositiveIntegerField()
	class Meta:
		db_table = 'Salesperson'

class Terminal(models.Model):
	city = models.CharField(max_length=20)
	address = models.CharField(max_length=100)
	phone = models.CharField(max_length=18)
	capacity = models.IntegerField()
	class Meta:
		db_table = 'Terminal'
		unique_together = (('city','address'),)

class TerminalAgent(models.Model):
	tck_no = models.ForeignKey(SystemUser,primary_key=True,db_column='tck_no')
	terminal_id = models.ForeignKey(Terminal,db_column='terminal_id',db_index=False)
	class Meta:
		db_table = 'TerminalAgent'

class Driver(models.Model):
	tck_no = models.ForeignKey(Staff,primary_key=True,db_column='tck_no')
	license_no = models.CharField(max_length=7)
	class Meta:
		db_table = 'Driver'

class BusType(models.Model):
	brand = models.CharField(max_length=20)
	model = models.CharField(max_length=20)
	year = models.CharField(max_length=4)
	layout = models.IntegerField()
	passenger_capacity = models.IntegerField()
	storage_capacity = models.DecimalField(max_digits=5,decimal_places=2)
	height = models.DecimalField(max_digits=3,decimal_places=2,null=True)
	width = models.DecimalField(max_digits=3,decimal_places=2,null=True)
	length = models.DecimalField(max_digits=3,decimal_places=1,null=True)
	class Meta:
		db_table = 'BusType'
		unique_together = (('brand','model','year'),)

class BusTypeFeature(models.Model):
	bustype_id = models.ForeignKey(BusType,db_column='bustype_id',db_index=False)
	feature_name = models.CharField(max_length=30)
	class Meta:
		db_table = 'BusTypeFeature'
		unique_together = (('bustype_id','feature_name'),)

class Bus(models.Model):
	plate = models.CharField(max_length=10,primary_key=True)
	bustype_id = models.ForeignKey(BusType,db_column='bustype_id',db_index=False)
	roaming_distance = models.IntegerField(default=0)
	start_date = models.DateField()
	is_operational = models.CharField(max_length=1,db_index=True)
	class Meta:
		db_table = 'Bus'
		unique_together = (('plate','bustype_id'),)

class Rent(models.Model):
	plate = models.ForeignKey(Bus,db_column='plate',db_index=False)
	start_time = models.DateField(auto_now_add=True) #raporda varchar(10) olarak gozukuyor
	end_time = models.DateField(null=True) #raporda varchar(10) olarak gorunuyor
	price = models.DecimalField(max_digits=6,decimal_places=2)
	rented_from = models.CharField(max_length=20)
	class Meta:
		db_table = 'Rent'
		unique_together = (('plate','start_time'),)

class RentedDriver(models.Model):
	tck_no = models.ForeignKey(Driver,db_column='tck_no',db_index=False)
	rent_id = models.ForeignKey(Rent,db_column='rent_id',db_index=False)
	class Meta:
		db_table = 'RentedDriver'
		unique_together = (('tck_no','rent_id'),)

class Assistant(models.Model):
	tck_no = models.ForeignKey(Staff,primary_key=True,db_column='tck_no')
	rank = models.CharField(max_length=20)
	class Meta:
		db_table = 'Assistant'

class RentedAssistant(models.Model):
	tck_no = models.ForeignKey(Assistant,db_column='tck_no',db_index=False)
	rent_id = models.ForeignKey(Rent,db_column='rent_id',db_index=False)
	class Meta:
		db_table = 'RentedAssistant'
		unique_together = (('tck_no','rent_id'),)

class Customer(models.Model):
	tck_no = models.CharField(max_length=11,primary_key=True,db_column='tck_no')
	name = models.CharField(max_length=35)
	surname = models.CharField(max_length=15)
	dateofbirth = models.DateField(null=True)
	gender = models.CharField(max_length=1)
	class Meta:
		db_table = 'Customer'

class RentedBy(models.Model):
	tck_no = models.ForeignKey(Customer,db_column='tck_no',db_index=False)
	plate = models.ForeignKey(Bus,db_column='plate',db_index=False)
	start_time = models.DateField(auto_now_add=True)
	class Meta:
		db_table = 'RentedBy'
		unique_together = (('tck_no','plate','start_time'),)

class Garage(models.Model):
	city = models.CharField(max_length=20)
	address = models.CharField(max_length=100)
	phone = models.CharField(max_length=18)
	class Meta:
		db_table = 'Garage'
		unique_together = (('city','address'),)

class IsAt(models.Model):
	garage_id = models.ForeignKey(Garage,db_column='garage_id',db_index=False)
	plate = models.ForeignKey(Bus,db_column='plate',db_index=True)
	class Meta:
		db_table = 'IsAt'
		unique_together = (('garage_id','plate'),)

class Route(models.Model):
	route_id = models.IntegerField(primary_key=True,db_column='route_id')
	depart_terminal = models.ForeignKey(Terminal,db_column='depart_terminal',related_name='+')#related_name is to prevent back pointer from terminal to route
	arrive_terminal = models.ForeignKey(Terminal,db_column='arrive_terminal',related_name='+')
	estimated_duration = models.IntegerField(null=True)
	distance = models.IntegerField()
	number_of_breaks = models.IntegerField(default=0)
	class Meta:
		db_table = 'Route'

class Stopover(models.Model):
	terminal_id = models.ForeignKey(Terminal,db_column='terminal_id',db_index=False)
	route_id = models.ForeignKey(Route,db_column='route_id',db_index=True)
	class Meta:
		db_table = 'Stopover'
		unique_together = (('terminal_id','route_id'),)

class ServiceArea(models.Model):
	address = models.CharField(max_length=100,primary_key=True,db_column='address')
	class Meta:
		db_table = 'ServiceArea'

class Break(models.Model):
	route_id = models.ForeignKey(Route,db_column='route_id',db_index=True)
	address = models.ForeignKey(ServiceArea,db_column='address',db_index=False)
	duration = models.IntegerField(db_index=False)
	class Meta:
		db_table = 'Break'
		unique_together = (('route_id','address'),)

class Voyage(models.Model):
	plate = models.ForeignKey(Bus,db_column='plate',db_index=False)
	route_id = models.ForeignKey(Route,db_column='route_id')
	departure_time = models.DateTimeField(db_index=True)
	arrival_time = models.DateTimeField(null=True)
	price = models.DecimalField(max_digits=5,decimal_places=2)
	occupied_seats = models.IntegerField(default=0)
	class Meta:
		db_table = 'Voyage'
		unique_together = (('plate','route_id','departure_time'),)

class Reservation(models.Model):
	tck_no = models.ForeignKey(Customer,db_column='tck_no',db_index=False)
	voyage_id = models.ForeignKey(Voyage,db_column='voyage_id',db_index=True)
	seat = models.CharField(max_length=3)
	time = models.TimeField()
	price = models.DecimalField(max_digits=5,decimal_places=2)
	class Meta:
		db_table = 'Reservation'
		unique_together = (('tck_no','voyage_id','seat'),)

class AssociatedDriver(models.Model):
	tck_no = models.ForeignKey(Customer,db_column='tck_no',db_index=False)
	voyage_id = models.ForeignKey(Voyage,db_column='voyage_id',db_index=True)
	class Meta:
		db_table = 'AssociatedDriver'
		unique_together = (('tck_no','voyage_id'),)

class AssociatedAssistant(models.Model):
	tck_no = models.ForeignKey(Customer,db_column='tck_no',db_index=False)
	voyage_id = models.ForeignKey(Voyage,db_column='voyage_id',db_index=True)
	class Meta:
		db_table = 'AssociatedAssistant'
		unique_together = (('tck_no','voyage_id'),)

class Ticket(models.Model):
	tck_no = models.ForeignKey(Customer,db_column='tck_no',db_index=False)
	voyage_id = models.ForeignKey(Voyage,db_column='voyage_id',db_index=True)
	seat = models.CharField(max_length=3)
	payment_type = models.CharField(max_length=5)
	payment_time = models.DateTimeField()
	price = models.DecimalField(max_digits=5,decimal_places=2)
	class Meta:
		db_table = 'Ticket'
		unique_together = (('tck_no','voyage_id','seat'),('voyage_id','seat'),)