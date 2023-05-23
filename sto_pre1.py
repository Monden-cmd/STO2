import unittest

class Vehicle:
    def __init__(self, vin, make, model):
        self.vin = vin
        self.make = make
        self.model = model
        self.service_history = []

    def add_service(self, service):
        self.service_history.append(service)

    def get_service_history(self):
        return self.service_history


class Service:
    def __init__(self, date, description):
        self.date = date
        self.description = description

vehicle = Vehicle("VIN123", "Honda", "Accord")
service1 = Service("2023-05-20", "Заміна масла")
service2 = Service("2023-05-22", "Заміна фільтра повітря")
vehicle.add_service(service1)
vehicle.add_service(service2)
service_history = vehicle.get_service_history()
for service in service_history:
    print(f"Дата: {service.date}, Опис: {service.description}")
