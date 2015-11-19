import unittest
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException


class GraphClientTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_save_graph_on_server(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")

        self.assertIn("Graph utils", driver.title)

        graph_input_area = driver.find_element_by_id("graphInputArea")
        graph_input_area.send_keys("nodes:1,2;arcs:1->2[9]")

        save_graph_button = driver.find_element_by_id("saveGraphButton")
        save_graph_button.send_keys(Keys.RETURN)

        # while(True):
        #     try:
        #         alert = driver.switch_to.alert
        #         break
        #     except NoAlertPresentException:
        #         driver.implicitly_wait(1) # wait 2 seconds for alert
        # print(alert.text)
        #
        # if re.search("^Saved with pk = [\d]+$", alert.text) is None:
        #     assert False

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
