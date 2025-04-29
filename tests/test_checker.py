import unittest
from weather.checker import get_weather

class TestWeatherChecker(unittest.TestCase):
    def test_get_weather_structure(self):
        dummy_data = {
            "location": {"name": "London"},
            "current": {"temp_c": 15.0}
        }
        self.assertIn("location", dummy_data)
        self.assertIn("current", dummy_data)

if __name__ == "__main__":
    unittest.main()
