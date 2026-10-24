import unittest
from monitor import get_status


class TestMonitor(unittest.TestCase):

    def test_low_usage(self):
        self.assertEqual(get_status(35), "HEALTHY")

    def test_usage_at_threshold(self):
        self.assertEqual(get_status(80), "HEALTHY")

    def test_usage_above_threshold(self):
        self.assertEqual(get_status(81), "WARNING")

    def test_very_high_usage(self):
        self.assertEqual(get_status(95), "WARNING")


if __name__ == "__main__":
    unittest.main()
