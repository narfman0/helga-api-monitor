import unittest
from unittest import TestCase
from helga_api_monitor.plugin import error_count


class TestEndpoint(TestCase):
    def test_errors(self):
        # this is a pretty dumb unit test, since it actually hits the endpoint, but whatever its convenience
        # and shows some of whats happening..?
        self.assertTrue(error_count() == 0)


if __name__ == '__main__':
    unittest.main()
