from django.db import models

class SchedChange(models.Model):

    pnr = models.CharField(primary_key=True,max_length=10)
    dk = models.CharField(max_length=30)
    cc_agent = models.CharField(max_length=30)
    t_pcc = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    pax_names = models.CharField(max_length=500,default = 'ANY', blank = True)
    is_ticket = models.BooleanField(default = False)
    booking_pcc = models.CharField(max_length=50,blank=True,null=True)
    booking_agent = models.CharField(max_length=50,blank=True,null=True)
    file_name = models.CharField(max_length=200,blank=True,null=True)
    departure_date = models.DateTimeField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.pnr + ' - ' + self.dk + ' by ' + self.booking_agent


class SegmentSched(models.Model):
    
    id = models.AutoField(primary_key=True)
    pnr = models.ForeignKey(SchedChange, on_delete = models.CASCADE)
    airline = models.CharField(max_length=50,blank=True,null=True)
    fligthno = models.CharField(max_length=50,blank=True,null=True)
    origin = models.CharField(max_length=50,blank=True,null=True)
    destination = models.CharField(max_length=50,blank=True,null=True)
    departure_date = models.DateTimeField(max_length=50,blank=True,null=True)
    arrival_date = models.DateTimeField(max_length=50,blank=True,null=True)
    status = models.CharField(max_length=50,blank=True,null=True)


class Passenger(models.Model):

    firstname = models.CharField(max_length = 50, blank = True)
    lastname = models.CharField(max_length = 50, blank = True)
    passenger_type = models.CharField(max_length = 10, blank = True)
    birthdate = models.DateField(null = True, blank = True)
    home_phone = models.CharField(max_length = 50, null = True, blank = True)
    email = models.CharField(max_length = 50, null = True, blank = True)
    address = models.CharField(max_length = 100, null = True, blank = True)
    city = models.CharField(max_length = 50, null = True, blank = True)
    country = models.CharField(max_length = 50, null = True, blank = True)
    state = models.CharField(max_length = 50, null = True, blank = True)
    zip_code = models.CharField(max_length = 20, null = True, blank = True)
    traveler_of = models.EmailField(null = True, blank = True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname
    
    class Meta:
        unique_together = ("firstname", "lastname", "birthdate")


class Reservation(models.Model):
    
    pnr = models.CharField(max_length=10, primary_key=True)
    airline = models.CharField(max_length=50,null=True)
    origin = models.CharField(max_length=100,null=True)
    destination = models.CharField(max_length=100,null=True)
    itinerary = models.CharField(max_length=100,null=True)
    departure_date = models.DateTimeField(null=True)
    return_date = models.DateTimeField(null=True)
    interface_id = models.CharField(max_length=30)
    payement_card = models.CharField(max_length=50,null=True)
    ticketing_pcc = models.CharField(max_length=50,null=True)
    ticketing_agent = models.CharField(max_length=50,null=True)
    ticket_issu_date = models.DateTimeField(blank=True,null=True)
    carriers = models.CharField(max_length=100,null=True)
    validating_carrier = models.CharField(max_length=100,null=True)
    class_of_service = models.CharField(max_length=50,null=True)
    frequent_flyer = models.CharField(max_length=50,blank=True,null=True)
    booking_pcc = models.CharField(max_length=50,blank=True,null=True)
    booking_agent = models.CharField(max_length=50,blank=True,null=True)
    is_ticketed = models.BooleanField (default=False)
    passengers = models.ManyToManyField(Passenger, related_name = 'passengers' , through='Travel')

    def __str__(self):
        return self.pnr + ' - ' + self.interface_id + ' by ' + self.booking_agent

class Travel(models.Model):
    pnr = models.ForeignKey(Reservation, on_delete = models.CASCADE)
    passenger =  models.ForeignKey(Passenger, on_delete = models.CASCADE)
    tkt_number = models.CharField(max_length = 50, null = True, blank = True)
    ticketing_issu_date = models.CharField(max_length = 50, null = True, )
    class Meta:
        unique_together = ("pnr", "passenger")

