import unittest

from python.src.lib.Main import Main


class TestMain(unittest.TestCase):
    def test_get_greeting(self):
        self.assertTrue(Main.get_greeting() == "Hello World!")
