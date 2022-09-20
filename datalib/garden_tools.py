import json
from data_interface import *


class GardenTools:

    data_inter = dataInterface()

    def __init__(self):
        self.data_inter = dataInterface()

    def get_garden_tools_json_data(self):
        data = self.data_inter.get_garden_tools()
        return data

    def get_garden_calender_json_data(self):
        pass

    def get_garden_post_json_data(self):
        pass


