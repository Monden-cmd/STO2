import unittest
from sto_pre1 import Vehicle, Service

class VehicleTestCase(unittest.TestCase):
    def test_get_service_history(self):
        vehicle = Vehicle("VIN123", "Honda", "Accord")
        service1 = Service("2023-05-20", "Заміна масла")
        service2 = Service("2023-05-22", "Заміна фільтра повітря")
        vehicle.add_service(service1)
        vehicle.add_service(service2)

        service_history = vehicle.get_service_history()

        self.assertEqual(len(service_history), 2)  # Перевіряємо, чи повертається історія з двома записами

        expected_results = [
            {"date": "2023-05-20", "description": "Заміна масла"},
            {"date": "2023-05-22", "description": "Заміна фільтра повітря"}
        ]
        for i, service in enumerate(service_history):
            self.assertEqual(service.date, expected_results[i]["date"])  # Перевіряємо дату
            self.assertEqual(service.description, expected_results[i]["description"])  # Перевіряємо опис


if __name__ == '__main__':
    unittest.main()
