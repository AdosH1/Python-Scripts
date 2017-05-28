#An automated selenium test designed to test the interface of a web calculator
# Available @ http://teaching.csse.uwa.edu.au/units/CITS5501/Assinments/calculator.html
# By Aden Huen

#Tests web interface by input space partitioning

import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

class test_webcalc(unittest.TestCase): 

    def test_input(self):
        #Tests the amount of digits allowed in calculator register
        input_size = 0
        alert_popped = False
        
        while (alert_popped == False):
            try:
                expected_conditions.alert_is_present()
                alert = driver.switch_to_alert()
                alert.accept()
                alert_popped = True
                
            except Exception:
                btn1.click()
                input_size += 1
                
        self.assertEqual(input_size, 17)
        btndel.click()
        
    def test_buttons_c(self):
        btndel.click()
        #Test all buttons besides del and =
        btn1.click()
        btndot.click()
        btn2.click()
        btnplus.click()
        btn3.click()
        btnminus.click()
        btn4.click()
        btntimes.click()
        btn5.click()
        btndivide.click()
        btn6.click()
        btnmod.click()
        btn7.click()
        btn8.click()
        btn9.click()
        btn0.click()
        self.assertEqual(result.text, '1.2+3-4*5/6%7890')
        #Test Del
        btndel.click()
        self.assertEqual(result.text, '')
        #Test =
        btndot.click()
        btnequal.click()
        self.assertEqual(result.text, '0')
        btndel.click()
        
    #Test putting zeros after each characteristic as zero is a special case number
    def test_zero_after_digit_c(self):
        btndel.click()
        btn4.click()
        btn0.click()
        self.assertEqual(result.text, '40')
        btndel.click()
    def test_zero_at_start_c(self):
        btndel.click()
        btn0.click()
        btndot.click()
        btn1.click()
        self.assertEqual(result.text, '0.1')
        btndel.click()
    def test_zero_after_decimal_c(self):
        btndel.click()
        btn1.click()
        btndot.click()
        btn0.click()
        btn1.click()
        self.assertEqual(result.text, '1.01')
        btndel.click()
    def test_zero_after_operator_c(self):
        btndel.click()
        btn1.click()
        btnplus.click()
        btn0.click()
        self.assertEqual(result.text, '1+0')
        btndel.click()
    
    def test_overflow_c(self): 
        btndel.click()    
        #Test Overflow
        # ENTER 99 999 999 * 9 999 999 EXPECT 
        btn9.click()
        btn9.click()
        btn9.click()
        btn9.click()
        btn9.click()
        btn9.click()
        btn9.click()
        btn9.click()
        btntimes.click()
        btn9.click()
        btn9.click()
        btn9.click()
        btn9.click()
        btn9.click()
        btn9.click()
        btn9.click()
        btnequal.click()
        self.assertEqual(result.text, '999999890000001')
        btndel.click()
        
    def test_underflow_c(self):
        btndel.click()
        #Test Underflow
        #ENTER '22/7' EXPECT 3.142857142857142 (17 character limit)
        btn2.click()
        btn2.click()
        btndivide.click()
        btn7.click()
        btnequal.click()
        self.assertEqual(result.text, '3.142857142857143')
        btndel.click()
        
    def test_bidmas_c(self):
        btndel.click()
        #Test BIDMAS
        # ENTER 1 + 6 * 4 / 2 - 3 EXPECTING 10
        btn1.click()
        btnplus.click()
        btn6.click()
        btntimes.click()
        btn4.click()
        btndivide.click()
        btn2.click()
        btnminus.click()
        btn3.click()
        btnequal.click()
        self.assertEqual(result.text, '10')
        btndel.click()

        

    # I will be using shorthand notation to explain each input
    # [digits] = 'd'
    # [decimal] = '.'
    # [operator] = 'o'
    # [evaluate] = 'e'
    # valid evaluation = 'V'
    # invalid evaluation = 'I'
    # where an evaluation is valid if the output is not nothing and is correct arithmetically
    
        
    ###>Test single characteristic evaluation
    def test_del(self):
        btndel.click()
        # Special case delete
        btn1.click()
        btndel.click()
        btnequal.click()
        self.assertEqual(result.text, '')
        btndel.click()
    def test_digit(self):  
        btndel.click()    
        # de = V
        btn1.click()
        btnequal.click()
        self.assertEqual(result.text, '1')
        btndel.click()
    def test_operator(self): 
        btndel.click()    
        # oe = I
        btnplus.click()
        btnequal.click()
        self.assertEqual(result.text, '')
        btndel.click()
    def test_decimal(self):  
        btndel.click()
        # .e = I
        btndot.click()
        btnequal.click()
        self.assertEqual(result.text, '0')
        btndel.click()
    def test_evaluator(self):   
        btndel.click()
        # e = I
        btnequal.click()
        self.assertEqual(result.text, '')
        btndel.click()
        
        ###>Test double characteristic evaluation
        # In order to avoid naming problems, we will be replacing decimal
        # with 'x' for describing our test
    def test_dx(self): 
        btndel.click()
        # d.e = I
        btn1.click()
        btndot.click()
        btnequal.click()
        self.assertEqual(result.text, '')
        btndel.click()
    def test_do(self):   
        btndel.click()
        # doe = I
        btn1.click()
        btnplus.click()
        btnequal.click()
        self.assertEqual(result.text, '')
        btndel.click()
    def test_xd(self):   
        btndel.click()
        # .de = V
        btndot.click()
        btn1.click()
        btnequal.click()
        self.assertEqual(result.text, '0.1')
        btndel.click()
    def test_xo(self):    
        btndel.click()
        # .oe = I
        btndot.click()
        btnplus.click()
        btnequal.click()
        self.assertEqual(result.text, '')
        btndel.click()
        
        # Starting with operator in single characteristic test fails,
        # Thus we do not need to consider operator first branches
        
        ###> Triple characteric evaluation
    def test_dxd(self): 
        btndel.click()
        # d.de = V
        btn1.click()
        btndot.click()
        btn1.click()
        btnequal.click()
        self.assertEqual(result.text, '1.1')
        btndel.click()
    def test_dxo_and_dox(self):   
        btndel.click()
        # d.oe = I / do.e = I
        btn1.click()
        btndot.click()
            #here and below we find inputing o after . will replace the . with the o
            # and inputing . after o does not change the register
            # thus, we do not need to consider (./o)-(./o) pairs
        self.assertEqual(result.text, '1.')
        btnplus.click()
        self.assertEqual(result.text, '1+')
        btndot.click()
        self.assertEqual(result.text, '1+')
        btnequal.click()
        self.assertEqual(result.text, '')
        btndel.click()
    def test_dxx(self):  
        btndel.click()
        # d..e = I
        btn1.click()
        btndot.click()
        self.assertEqual(result.text, '1.')
        btndot.click() #the decimal does not add anything into the register
        self.assertEqual(result.text, '1.') #thus, we do not need to consider decimal-decimal pairs
        btnequal.click()
        self.assertEqual(result.text, '')
        btndel.click()
    def test_dod(self):   
        btndel.click()
        # dode = V
        btn1.click()
        btnplus.click()
        btn1.click()
        btnequal.click()
        self.assertEqual(result.text, '2')
        btndel.click()
    def test_dox(self): 
        btndel.click()
        # do.e = I
        btn1.click()
        btnplus.click()
        btndot.click()
        btnequal.click()
        self.assertEqual(result.text, '')
        btndel.click()
    def test_doo(self):    
        btndel.click()
        # dooe = V
        btn1.click()
        btnplus.click()
        self.assertEqual(result.text, '1+')
        btnminus.click() #the operator replaces previous operator
        self.assertEqual(result.text, '1-') #thus, we do not need to consider operator-operator pairs
        btnequal.click() 
        self.assertEqual(result.text, '')
        btndel.click()
    def test_xdo(self):   
        btndel.click()
        # .doe = I
        btndot.click()
        btn1.click()
        btnplus.click()
        btnequal.click()
        self.assertEqual(result.text, '')
        btndel.click()
    def test_xdx(self):     
        btndel.click()
        # .d.e = I
        btndot.click()
        btn1.click()
        btndot.click()
        btnequal.click()
        self.assertEqual(result.text, '')
        btndel.click()
        
        ###> Quadruple characteristic evaluation
    def test_dodx(self): 
        btndel.click()
        # dod.e = I
        btn1.click()
        btnplus.click()
        btn1.click()
        btndot.click()
        btnequal.click()
        self.assertEqual(result.text, '')
        btndel.click()
    def test_dodo(self):    
        btndel.click()
        # dodoe = I
        btn1.click()
        btnplus.click()
        btn1.click()
        btnplus.click()
        btnequal.click()
        self.assertEqual(result.text, '')
        btndel.click()
    def test_xdod(self):  
        btndel.click()
        # .dode = V
        btndot.click()
        btn1.click()
        btnplus.click()
        btn1.click()
        btnequal.click()
        self.assertEqual(result.text, '1.1')
        btndel.click()
    def test_xdxd(self):
        btndel.click()
        # .d.de = I
        btndot.click()
        btn1.click()
        btndot.click()
        btn1.click()
        btnequal.click()
        self.assertEqual(result.text, '')
        btndel.click()
        
        ###> Quintuple characteristic evaluation
    def test_dodod(self): 
        btndel.click()
        # dodode = V
        btn1.click()
        btnplus.click()
        btn1.click()
        btnplus.click()
        btn1.click()
        btnequal.click()
        self.assertEqual(result.text, '3')
        btndel.click()
    def test_dxdod(self):     
        btndel.click()
        # d.dode = V
        btn1.click()
        btndot.click()
        btn1.click()
        btnplus.click()
        btn1.click()
        btnequal.click()
        self.assertEqual(result.text, '2.1')
        btndel.click()
    def test_dodxd(self):  
        btndel.click()
        # dod.de = V
        btn1.click()
        btnplus.click()
        btn1.click()
        btndot.click()
        btn1.click()
        btnequal.click()
        self.assertEqual(result.text, '2.1')
        btndel.click()
    def test_xdodx(self):     
        btndel.click()
        # .dod.e = I
        btndot.click()
        btn1.click()
        btnplus.click()
        btn1.click()
        btndot.click()
        btnequal.click()
        self.assertEqual(result.text, '')
        btndel.click()
    def test_xdodo(self):   
        btndel.click()
        # .dodoe = I
        btndot.click()
        btn1.click()
        btnplus.click()
        btn1.click()
        btnplus.click()
        btnequal.click()
        self.assertEqual(result.text, '')
        btndel.click()
    def test_xdxdo(self):    
        btndel.click()
        # .d.doe = I
        btndot.click()
        btn1.click()
        btndot.click()
        btn1.click()
        btnplus.click()
        btnequal.click()
        self.assertEqual(result.text, '')
        btndel.click()
    def test_xdxdx(self):     
        btndel.click()
        # .d.d.e = I
        btndot.click()
        btn1.click()
        btndot.click()
        btn1.click()
        btndot.click()
        btnequal.click()
        self.assertEqual(result.text, '')
        btndel.click()
        
        # Here we can assume that besides having a decimal as the first input,
        # decimals need to be in the form d.d or they will
        # reset the register, we can omit them from further branches
        
        ###> Sextuple characteristic evaluation
    def test_xdodxd(self): 
        btndel.click()
        # .dod.de = V
        btndot.click()
        btn1.click()
        btnplus.click()
        btn1.click()
        btndot.click()
        btn1.click()
        btnequal.click()
        self.assertEqual(result.text, '1.2')
        btndel.click()

        ###> Septuple characteristic evaluation
    def test_dxdodxd(self): 
        btndel.click()
        # d.dod.de = V
        btn1.click()
        btndot.click()
        btn1.click()
        btnplus.click()
        btn1.click()
        btndot.click()
        btn1.click()
        btnequal.click()
        self.assertEqual(result.text, '2.2')
        btndel.click()
    def test_dododod(self):   
        btndel.click()
        # dododode = V
        btn1.click()
        btnplus.click()
        btn1.click()
        btnplus.click()
        btn1.click()
        btnplus.click()
        btn1.click()
        btnequal.click()
        self.assertEqual(result.text, '4')
        btndel.click()
    def test_dodxdod(self):   
        btndel.click()
        # dod.dode = V
        btn1.click()
        btnplus.click()
        btn1.click()
        btndot.click()
        btn1.click()
        btnplus.click()
        btn1.click()
        btnequal.click()
        self.assertEqual(result.text, '3.1')
        btndel.click()
        
        # Here we can see the test has devolved into having permutations with every 
        # second characteristic is digit, we can simplify the problem by also noting
        # that only one decimal can be present between operators


if __name__ == "__main__":
    #Use chrome webdriver
    driver = webdriver.Chrome()
    #Go to target website
    driver.get("http://teaching.csse.uwa.edu.au/units/CITS5501/Assignments/calculator.html")

    #map buttons for testing
    btn1 = driver.find_element_by_xpath("//button[@value='1']")
    btn2 = driver.find_element_by_xpath("//button[@value='2']")
    btn3 = driver.find_element_by_xpath("//button[@value='3']")
    btn4 = driver.find_element_by_xpath("//button[@value='4']")
    btn5 = driver.find_element_by_xpath("//button[@value='5']")
    btn6 = driver.find_element_by_xpath("//button[@value='6']")
    btn7 = driver.find_element_by_xpath("//button[@value='7']")
    btn8 = driver.find_element_by_xpath("//button[@value='8']")
    btn9 = driver.find_element_by_xpath("//button[@value='9']")
    btn0 = driver.find_element_by_xpath("//button[@value='0']")
    btnplus = driver.find_element_by_xpath("//button[@value='+']")
    btnminus = driver.find_element_by_xpath("//button[@value='-']")
    btntimes = driver.find_element_by_xpath("//button[@value='*']")
    btndivide = driver.find_element_by_xpath("//button[@value='/']")
    btnequal = driver.find_element_by_xpath("//button[@value='=']")
    btndot = driver.find_element_by_xpath("//button[@value='.']")
    btnmod = driver.find_element_by_xpath("//button[@value='%']")
    btndel = driver.find_element_by_id("delete")
    result = driver.find_element_by_id("result")

    unittest.main(exit=False)
    
    driver.close()
