from django.db import models
from django.db.models import PROTECT


class ClientNames(models.Model):
    # id_client_names = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15, null=True, blank=True)
    last_name = models.CharField(max_length=15, null=True, blank=True)
    patronymic = models.CharField(max_length=20, null=True, blank=True)
    name_of_organization = models.CharField(max_length=30, null=True, blank=True)

    class Type(models.TextChoices):
        individuals = 'FZ'
        entities = 'UR'

    type = models.CharField(max_length=2, choices=Type.choices)

    def __str__(self):
        return '%s %s %s %s, %s' % (self.name, self.last_name, self.patronymic,
                                    self.name_of_organization, self.type)


class ClientAddress(models.Model):
    # id_client_names = models.AutoField(primary_key=True)
    country = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    street = models.CharField(max_length=20)
    house_number = models.CharField(max_length=10)
    apartment_number = models.CharField(max_length=10)
    index = models.CharField(max_length=10)

    def __str__(self):
        return '%s, %s, %s, %s, %s, %s' % (self.country, self.city, self.street,
                                           self.house_number, self.apartment_number, self.index)


class Client(models.Model):
    client_names = models.ForeignKey(ClientNames, on_delete=PROTECT)
    client_address = models.ForeignKey(ClientAddress, on_delete=PROTECT)
    email = models.EmailField(max_length=30)
    phone_number = models.SmallIntegerField(max_length=10)
    # PROTECT как я понимаю для тогл чтобы избежать удпления того на что ссылается


class Driver(models.Model):
    name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    patronymic = models.CharField(max_length=20, null=True, blank=True)
    driver_license = models.CharField(max_length=20)
    salary = models.SmallIntegerField(max_length=7)  # ЗП
    date_of_employment = models.DateField()


class Car(models.Model):
    Car_brand = models.CharField(max_length=15)
    Car_model = models.CharField(max_length=15)
    Car_color = models.CharField(max_length=10)
    Government_number = models.CharField(max_length=7)
    Inspection_date = models.DateField()
    Carrying_capacity = models.SmallIntegerField(max_length=5)  # Грузоподъемность
    Fuel_consumption_per_100_km = models.SmallIntegerField(max_length=3)
# class Receipt(models.Model):
#    client = models.ForeignKey(Client, on_delete=PROTECT)
