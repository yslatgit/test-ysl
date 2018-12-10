from selenium import webdriver
import unittest

class NewViditorTest(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.implicitly_wait(3)

    def tearDown(self):
        self.dr.quit()

    def test_t(self):
        self.dr.get("http://localhost:8000")
        self.assertIn("TODO",self.dr.title)
        self.fail("Finish the test")

if __name__ == '__main__':
    unittest.main(warnings="ignore")
