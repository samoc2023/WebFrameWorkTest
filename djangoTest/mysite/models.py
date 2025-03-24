from django.db import models

class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    for_sale = models.BooleanField(default=True)  # "Y/N" field replaced by boolean

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state_province = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Salesperson(models.Model):
    salesperson_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SalesInvoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    invoice_number = models.CharField(max_length=50)
    date = models.DateField()
    car_price = models.DecimalField(max_digits=10, decimal_places=2)
    # Foreign Keys
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.car} for {self.customer}"


class Mechanic(models.Model):
    mechanic_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ServiceTicket(models.Model):
    service_ticket_id = models.AutoField(primary_key=True)
    service_ticket_number = models.CharField(max_length=50)
    date_in = models.DateField()
    date_out = models.DateField(null=True, blank=True)
    payment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date_returned_to_customer = models.DateField(null=True, blank=True)
    # Foreign Keys
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Service Ticket #{self.service_ticket_number}"


class ServiceMechanic(models.Model):
    service_mechanic_id = models.AutoField(primary_key=True)
    # Foreign Keys
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)

    def __str__(self):
        return f"Mechanic {self.mechanic} on Ticket {self.service_ticket}"


class Parts(models.Model):
    parts_id = models.AutoField(primary_key=True)
    part_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.part_name


class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.service_name


class PartsUsed(models.Model):
    parts_used_id = models.AutoField(primary_key=True)
    # Foreign Keys
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    part = models.ForeignKey(Parts, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.part} on {self.service_ticket}"
