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


class STO:
    def __init__(self):
        self.vehicles = []
        self.orders = {}
        self.parts_orders = {}

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def create_order(self, vehicle_vin, order_number):
        self.orders[order_number] = vehicle_vin

    def create_parts_order(self, parts_order_number, parts):
        self.parts_orders[parts_order_number] = parts

    def get_vehicle_service_history(self, vin):
        for vehicle in self.vehicles:
            if vehicle.vin == vin:
                return vehicle.service_history
        return None

    def get_order_vehicle_service_history(self, order_number):
        vehicle_vin = self.orders.get(order_number)
        if vehicle_vin:
            return self.get_vehicle_service_history(vehicle_vin)
        return None

    def get_parts_order(self, parts_order_number):
        return self.parts_orders.get(parts_order_number)


sto = STO()
vehicle1 = Vehicle("VIN123", "Honda", "Accord")
vehicle2 = Vehicle("VIN456", "Toyota", "Camry")
sto.add_vehicle(vehicle1)
sto.add_vehicle(vehicle2)
service1 = Service("2023-05-20", "Заміна масла")
service2 = Service("2023-05-22", "Заміна фільтра повітря")
vehicle1.add_service(service1)
vehicle2.add_service(service2)
sto.create_order("VIN123", "ORD001")
sto.create_order("VIN456", "ORD002")
sto.create_parts_order("PARTS001", ["Масляний фільтр", "Повітряний фільтр", "Свічки запалювання"])

# Отримати історію обслуговування для конкретного транспортного засобу
vehicle_history = sto.get_vehicle_service_history("VIN123")
print("Історія обслуговування для транспортного засобу з VIN VIN123:")
for service in vehicle_history:
    print(f"Дата: {service.date}, Опис: {service.description}")

# Отримати історію обслуговування за номером замовлення
order_history = sto.get_order_vehicle_service_history("ORD002")
print("Історія обслуговування для замовлення з номером ORD002:")
if order_history:
    for service in order_history:
        print(f"Дата: {service.date}, Опис: {service.description}")
else:
    print("Замовлення з таким номером не знайдено")

# Отримати деталі замовлення запчастин
parts_order = sto.get_parts_order("PARTS001")
if parts_order:
    print(f"Деталі замовлення запчастин з номером PARTS001:")
    for part in parts_order:
        print(part)
else:
    print("Замовлення запчастин з таким номером не знайдено")

