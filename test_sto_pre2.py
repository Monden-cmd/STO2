import unittest
from sto_pre2 import Vehicle, Service, STO

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

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def create_order(self, vehicle_vin, order_number):
        self.orders[order_number] = vehicle_vin

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


class STOTestCase(unittest.TestCase):
    def setUp(self):
        self.sto = STO()
        self.vehicle1 = Vehicle("VIN123", "Honda", "Accord")
        self.vehicle2 = Vehicle("VIN456", "Toyota", "Camry")
        self.sto.add_vehicle(self.vehicle1)
        self.sto.add_vehicle(self.vehicle2)
        self.service1 = Service("2023-05-20", "Заміна масла")
        self.service2 = Service("2023-05-22", "Заміна фільтра повітря")
        self.vehicle1.add_service(self.service1)
        self.vehicle2.add_service(self.service2)
        self.sto.create_order("VIN123", "ORD001")
        self.sto.create_order("VIN456", "ORD002")

    def test_get_vehicle_service_history(self):
        vehicle_history = self.sto.get_vehicle_service_history("VIN123")
        self.assertIsNotNone(vehicle_history)
        self.assertEqual(len(vehicle_history), 1)
        self.assertEqual(vehicle_history[0].date, "2023-05-20")
        self.assertEqual(vehicle_history[0].description, "Заміна масла")

    def test_get_order_vehicle_service_history(self):
        order_history = self.sto.get_order_vehicle_service_history("ORD002")
        self.assertIsNotNone(order_history)
        self.assertEqual(len(order_history), 1)
        self.assertEqual(order_history[0].date, "2023-05-22")
        self.assertEqual(order_history[0].description, "Заміна фільтра повітря")


if __name__ == '__main__':
    unittest.main()
