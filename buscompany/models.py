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
		db_table = 'staff'

class SystemUser(models.Model):
	staff = models.ForeignKey(Staff,primary_key=True,db_column='tck_no')
	user = models.OneToOneField(User)
	class Meta:
		db_table = 'systemuser'

class Manager(models.Model):
	system_user = models.ForeignKey(SystemUser,primary_key=True,db_column='tck_no')
	position = models.CharField(max_length=40)
	class Meta:
		db_table = 'manager'

class SalesOffice(models.Model):
	city = models.CharField(max_length=20)
	address = models.CharField(max_length=100)
	phone = models.CharField(max_length=18)
	class Meta:
		db_table = 'sales_office'
		unique_together = (('city','address'),)

class Salesperson(models.Model):
	system_user = models.ForeignKey(SystemUser,primary_key=True,db_column='tck_no')
	sales_office = models.ForeignKey(SalesOffice,db_column='office_id',db_index=True)
	tickets_sold = models.PositiveIntegerField()
	class Meta:
		db_table = 'salesperson'

class Terminal(models.Model):
	name = models.CharField(max_length=20)
	city = models.CharField(max_length=20)
	address = models.CharField(max_length=100)
	phone = models.CharField(max_length=18)
	capacity = models.IntegerField()
	class Meta:
		db_table = 'terminal'
		unique_together = (('city','address'),)

class TerminalAgent(models.Model):
	system_user = models.ForeignKey(SystemUser,primary_key=True,db_column='tck_no')
	terminal = models.ForeignKey(Terminal,db_column='terminal_id',db_index=False)
	class Meta:
		db_table = 'terminal_agent'

class Driver(models.Model):
	staff = models.ForeignKey(Staff,primary_key=True,db_column='tck_no')
	license_no = models.CharField(max_length=7)
	class Meta:
		db_table = 'driver'

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
		db_table = 'bus_type'
		unique_together = (('brand','model','year'),)

class BusTypeFeature(models.Model):
	bus_type = models.ForeignKey(BusType,db_column='bustype_id',db_index=False)
	feature_name = models.CharField(max_length=30)
	class Meta:
		db_table = 'bus_type_feature'
		unique_together = (('bus_type','feature_name'),)

class Bus(models.Model):
	plate = models.CharField(max_length=10,primary_key=True)
	bus_type = models.ForeignKey(BusType,db_column='bustype_id',db_index=False)
	roaming_distance = models.IntegerField(default=0)
	start_date = models.DateField()
	is_operational = models.CharField(max_length=1,db_index=True)
	class Meta:
		db_table = 'bus'
		unique_together = (('plate','bus_type'),)

class Rent(models.Model):
	bus = models.ForeignKey(Bus,db_column='plate',db_index=False)
	start_time = models.DateField(auto_now_add=True) #raporda varchar(10) olarak gozukuyor
	end_time = models.DateField(null=True) #raporda varchar(10) olarak gorunuyor
	price = models.DecimalField(max_digits=6,decimal_places=2)
	rented_from = models.CharField(max_length=20)
	class Meta:
		db_table = 'rent'
		unique_together = (('bus','start_time'),)

class RentedDriver(models.Model):
	driver = models.ForeignKey(Driver,db_column='tck_no',db_index=False)
	rent = models.ForeignKey(Rent,db_column='rent_id',db_index=False)
	class Meta:
		db_table = 'rented_driver'
		unique_together = (('driver','rent'),)

class Assistant(models.Model):
	staff = models.ForeignKey(Staff,primary_key=True,db_column='tck_no')
	rank = models.CharField(max_length=20)
	class Meta:
		db_table = 'assistant'

class RentedAssistant(models.Model):
	assistant = models.ForeignKey(Assistant,db_column='tck_no',db_index=False)
	rent = models.ForeignKey(Rent,db_column='rent_id',db_index=False)
	class Meta:
		db_table = 'rented_assistant'
		unique_together = (('assistant','rent'),)

class Customer(models.Model):
	tck_no = models.CharField(max_length=11,primary_key=True,db_column='tck_no')
	name = models.CharField(max_length=35)
	surname = models.CharField(max_length=15)
	dateofbirth = models.DateField(null=True)
	gender = models.CharField(max_length=1)
	class Meta:
		db_table = 'customer'

class RentedBy(models.Model):
	customer = models.ForeignKey(Customer,db_column='tck_no',db_index=False)
	bus = models.ForeignKey(Bus,db_column='plate',db_index=False)
	start_time = models.DateField(auto_now_add=True)
	class Meta:
		db_table = 'rented_by'
		unique_together = (('customer','bus','start_time'),)

class Garage(models.Model):
	city = models.CharField(max_length=20)
	address = models.CharField(max_length=100)
	phone = models.CharField(max_length=18)
	class Meta:
		db_table = 'garage'
		unique_together = (('city','address'),)

class IsAt(models.Model):
	garage = models.ForeignKey(Garage,db_column='garage_id',db_index=False)
	bus = models.ForeignKey(Bus,db_column='plate',db_index=True)
	class Meta:
		db_table = 'is_at'
		unique_together = (('garage','bus'),)

class Route(models.Model):
	route_id = models.IntegerField(primary_key=True,db_column='route_id')
	depart_terminal = models.ForeignKey(Terminal,db_column='depart_terminal',related_name='+')#related_name is to prevent back pointer from terminal to route
	arrive_terminal = models.ForeignKey(Terminal,db_column='arrive_terminal',related_name='+')
	estimated_duration = models.IntegerField(null=True)
	distance = models.IntegerField()
	number_of_breaks = models.IntegerField(default=0)
	class Meta:
		db_table = 'route'

class Stopover(models.Model):
	terminal = models.ForeignKey(Terminal,db_column='terminal_id',db_index=False)
	route = models.ForeignKey(Route,db_column='route_id',db_index=True)
	class Meta:
		db_table = 'stopover'
		unique_together = (('terminal','route'),)

class ServiceArea(models.Model):
	address = models.CharField(max_length=100,primary_key=True,db_column='address')
	class Meta:
		db_table = 'service_area'

class Break(models.Model):
	route = models.ForeignKey(Route,db_column='route_id',db_index=True)
	service_area = models.ForeignKey(ServiceArea,db_column='address',db_index=False)
	duration = models.IntegerField(db_index=False)
	class Meta:
		db_table = 'break'
		unique_together = (('route','service_area'),)

class Voyage(models.Model):
	bus = models.ForeignKey(Bus,db_column='plate',db_index=False)
	route = models.ForeignKey(Route,db_column='route_id')
	departure_time = models.DateTimeField(db_index=True)
	arrival_time = models.DateTimeField(null=True)
	price = models.DecimalField(max_digits=5,decimal_places=2)
	occupied_seats = models.IntegerField(default=0)
	class Meta:
		db_table = 'voyage'
		unique_together = (('bus','route','departure_time'),)

class Reservation(models.Model):
	customer = models.ForeignKey(Customer,db_column='tck_no',db_index=False)
	voyage = models.ForeignKey(Voyage,db_column='voyage_id',db_index=True)
	seat = models.CharField(max_length=3)
	time = models.TimeField()
	price = models.DecimalField(max_digits=5,decimal_places=2)
	class Meta:
		db_table = 'reservation'
		unique_together = (('customer','voyage','seat'),)

class AssociatedDriver(models.Model):
	customer = models.ForeignKey(Customer,db_column='tck_no',db_index=False)
	voyage = models.ForeignKey(Voyage,db_column='voyage_id',db_index=True)
	class Meta:
		db_table = 'associated_driver'
		unique_together = (('customer','voyage'),)

class AssociatedAssistant(models.Model):
	customer = models.ForeignKey(Customer,db_column='tck_no',db_index=False)
	voyage = models.ForeignKey(Voyage,db_column='voyage_id',db_index=True)
	class Meta:
		db_table = 'associated_assistant'
		unique_together = (('customer','voyage'),)

class Ticket(models.Model):
	customer = models.ForeignKey(Customer,db_column='tck_no',db_index=False)
	voyage = models.ForeignKey(Voyage,db_column='voyage_id',db_index=True)
	seat = models.CharField(max_length=3)
	payment_type = models.CharField(max_length=5)
	payment_time = models.DateTimeField()
	price = models.DecimalField(max_digits=5,decimal_places=2)
	class Meta:
		db_table = 'ticket'
		unique_together = (('customer','voyage','seat'),)
