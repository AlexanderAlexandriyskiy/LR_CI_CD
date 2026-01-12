import unittest
from car import Car, TooMuchFuelError, NotEnoughFuelError

class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("Test", 80)

    def test_empty_on_start(self):
        self.assertEqual(self.car.get_current_fuel_level(), 0)

    def test_refuel_30(self):
        self.car.refuel_car(30)
        self.assertEqual(self.car.get_current_fuel_level(), 30)

    def test_refuel_50(self):
        self.car.refuel_car(50)
        self.assertEqual(self.car.get_current_fuel_level(), 50)

    def test_drive_without_fuel(self):
        with self.assertRaises(NotEnoughFuelError):
            self.car.drive(20)

    def test_drive_with_fuel(self):
        self.car.refuel_car(50)
        remaining = self.car.drive(20)
        self.assertEqual(remaining, 50 - (8 * 20 / 100))
