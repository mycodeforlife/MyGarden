from datalib import data_interface


class GardenTools:

    data_inter = data_interface.DataInterface()

    def __init__(self):
        self.data_inter = data_interface.DataInterface()

    def get_garden_tools_json_data(self):
        data = self.data_inter.get_garden_tools()
        return data

    def get_garden_calender_json_data(self):
        pass

    def get_garden_post_json_data(self):
        pass

    def garden_tools_json_validator(self,data):
        pass

