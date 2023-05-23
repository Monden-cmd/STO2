import unittest
from sto import Vehicle, Service, STO

class VehicleTest(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle("VIN123", "Honda", "Accord")
        self.service1 = Service("2023-05-20", "Заміна масла")
        self.service2 = Service("2023-05-22", "Заміна фільтра повітря")

    def test_add_service(self):
        self.vehicle.add_service(self.service1)
        self.assertEqual(len(self.vehicle.service_history), 1)
        self.assertEqual(self.vehicle.service_history[0], self.service1)

    def test_get_service_history(self):
        self.vehicle.add_service(self.service1)
        self.vehicle.add_service(self.service2)
        service_history = self.vehicle.get_service_history()
        self.assertEqual(len(service_history), 2)
        self.assertEqual(service_history[0], self.service1)
        self.assertEqual(service_history[1], self.service2)

class STOTest(unittest.TestCase):
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
        self.sto.create_parts_order("PARTS001", ["Масляний фільтр", "Повітряний фільтр", "Свічки запалювання"])

    def test_get_vehicle_service_history(self):
        vehicle_history = self.sto.get_vehicle_service_history("VIN123")
        self.assertEqual(len(vehicle_history), 1)
        self.assertEqual(vehicle_history[0], self.service1)

    def test_get_order_vehicle_service_history(self):
        order_history = self.sto.get_order_vehicle_service_history("ORD002")
        self.assertEqual(len(order_history), 1)
        self.assertEqual(order_history[0], self.service2)

    def test_get_parts_order(self):
        parts_order = self.sto.get_parts_order("PARTS001")
        self.assertIsNotNone(parts_order)
        self.assertEqual(len(parts_order), 3)
        self.assertEqual(parts_order[0], "Масляний фільтр")
        self.assertEqual(parts_order[1], "Повітряний фільтр")
        self.assertEqual(parts_order[2], "Свічки запалювання")

if __name__ == '__main__':
    unittest.main()
