import unittest
from data_interface import dataInterface

class DataInterfaceTest(unittest.TestCase):

    data_interface = dataInterface()

    def test_mysql_connection(self):
        pass

    def test_get_garden_tools(self):
        # data = self.data_interface.get_garden_tools()
        pass

    def test_get_garden_calender(self):
        pass

    def test_get_recent_posts(self):
        pass


if __name__ == '__main__':
    unittest.main()
