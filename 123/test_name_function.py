import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """测试name_function.py"""
    def test_first_last_name(self):
        formatted_name = get_formatted_name("y","sl")
        self.assertEqual(formatted_name,'ysl')
    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name("q","c","s")
        self.assertEqual(formatted_name,'qsc')

if __name__ == '__main__':
    unittest.main()