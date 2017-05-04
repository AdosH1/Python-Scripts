#A unit test designed for the back end logic of a web calculator
# Available @ http://teaching.csse.uwa.edu.au/units/CITS5501/Assinments/calculator.html
# By Aden Huen

# Work in progress

import unittest
from calc import *

class test_calc(unittest.TestCase):
    
    #FUNCTION UNIT TESTING
    
    #check that the calculator initialises with correct variable properties
    def test_initialisation(self):
        x = Calculator()
        self.assertEqual(x.register, None)
        self.assertEqual(x.operation, None)
    
    #function sets the operator for input
    def test_set_op(self):
        x = Calculator()
        
        #check that the operation changes as required
        x.set_op('+')
        self.assertEqual(x.operation, '+')
        x.set_op('-')
        self.assertEqual(x.operation, '-')
        x.set_op('*')
        self.assertEqual(x.operation, '*')
        x.set_op('/')
        self.assertEqual(x.operation, '/')
        
        #includes no arguments
        x.set_op()
        self.assertRaises(TypeError)
        
        #includes whitespace
        x.set_op(' + ')
        self.assertEqual(x.operation, '+')
        
        #includes special characters
        x.set_op('ブレク')
        self.assertRaises(Exception)
        x.set_op('"/^%$@#*&/,.<>|][')
        self.assertRaises(Exception)
        
        #input overflow
        x.set_op('a'*2049)
        self.assertRaises(Exception)
        x.set_op(10**28)
        self.assertRaises(TypeError)
        
    #function sets the register number OR if number already exists, performs operation on new number
    def test_set_number(self):
        x = Calculator()
        
        #Input overflow
        x.set_number(10**28)
        self.assertEqual(x.register, 10**28)
        x.set_op('*')
        x.set_number(10**28)
        self.assertEqual(x.register, (10**28)*(10**28))
        x.clear()
        
        #Input underflow
        x.set_number(0.00000000000000000000000000001)
        self.assertEqual(x.register, 0.00000000000000000000000000001)
        x.set_op('+')
        x.set_number(1)
        self.assertEqual(x.register, 1.00000000000000000000000000001)
        
        
        
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    unittest.main()