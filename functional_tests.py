import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        # check out the home page here: 
        self.browser.get("http://localhost:8000")
        
        # notices the page title and header mention to do lists: 
        self.assertIn("To-Do", self.browser.title)

        # she is invited to enter to do item straight away: 
        self.fail("Finish the test!")


if __name__ == "__main__":
    unittest.main()