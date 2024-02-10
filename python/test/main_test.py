from python.src.main import Main
import unittest


class TestMain(unittest.TestCase):
    def test_get_greeting(self):
        self.assertTrue(Main.get_greeting() == "Hello World!")
