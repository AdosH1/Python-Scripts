#An automated selenium test designed to test the interface of a web calculator
# Available @ http://teaching.csse.uwa.edu.au/units/CITS5501/Assinments/calculator.html
# By Aden Huen

# Work in progress

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class test_webcalc(unittest.TestCase):
    
    def setUp(self): 
        #Use chrome webdriver
        self.driver = webdriver.Chrome()
        #Go to target website
        self.driver.get("http://teaching.csse.uwa.edu.au/units/CITS5501/Assignments/calculator.html")
        
        #map buttons for testing
        self.btn1 = self.driver.find_element_by_xpath("//button[@value='1']")
        self.btn2 = self.driver.find_element_by_xpath("//button[@value='2']")
        self.btn3 = self.driver.find_element_by_xpath("//button[@value='3']")
        self.btn4 = self.driver.find_element_by_xpath("//button[@value='4']")
        self.btn5 = self.driver.find_element_by_xpath("//button[@value='5']")
        self.btn6 = self.driver.find_element_by_xpath("//button[@value='6']")
        self.btn7 = self.driver.find_element_by_xpath("//button[@value='7']")
        self.btn8 = self.driver.find_element_by_xpath("//button[@value='8']")
        self.btn9 = self.driver.find_element_by_xpath("//button[@value='9']")
        self.btn0 = self.driver.find_element_by_xpath("//button[@value='0']")
        self.btnplus = self.driver.find_element_by_xpath("//button[@value='+']")
        self.btnminus = self.driver.find_element_by_xpath("//button[@value='-']")
        self.btntimes = self.driver.find_element_by_xpath("//button[@value='*']")
        self.btndivide = self.driver.find_element_by_xpath("//button[@value='/']")
        self.btnequal = self.driver.find_element_by_xpath("//button[@value='=']")
        self.btndot = self.driver.find_element_by_xpath("//button[@value='.']")
        self.btnmod = self.driver.find_element_by_xpath("//button[@value='%']")
        self.btndel = self.driver.find_element_by_id("delete")
        self.result = self.driver.find_element_by_id("result")
    
    
    def test_arithmatic(self):  
        #Check webpage title has our assignment title
        self.assertIn("CITS5501 Automation Assignment", self.driver.title)
        
        #Test BIDMAS
        # ENTER 1 + 2 * 3 EXPECTING 7
        self.btn1.click()
        self.btnplus.click()
        self.btn2.click()
        self.btntimes.click()
        self.btn3.click()
        self.btnequal.click()
        self.assertEqual(self.result.text, '7')
     
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
