import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        # Edith has heard about a cool new online to do app.
        # She check out the home page here: 
        self.browser.get("http://localhost:8000")
        
        # She notices the page title and header mention to do lists: 
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)


        # she is invited to enter to do item straight away: 
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder", "Enter a to-do item"))

        # She types "Buy peacock feathers" into a text box
        # (Edith's hobby is typing fly-fishing lures)
        inputbox.send_ikeys(Keys.ENTER)
        time.sleep(1)

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly"
        # (Edith is very methodical)
        self.fail("Finish the test!")

        # The page updates again, and now shows both items on her list
        # ...

if __name__ == "__main__":
    unittest.main()