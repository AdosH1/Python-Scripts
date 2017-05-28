#A unit test designed for the back end logic of a web calculator
# Available @ http://teaching.csse.uwa.edu.au/units/CITS5501/Assinments/calculator.html
# By Aden Huen

#methods ending with 'c' are deemed critical for the operation of the calculator
# methods ending with 'n' are deemed non-critical

import unittest
from calc import *

class test_calc(unittest.TestCase):
   
    #########################> UNIT TESTING <#########################
    
    ######################### CRITICAL TESTS #########################
    # These tests assume a 17 character display for the web calculator
    # (All these tests contain maximum 17 characters)
    
    # Initialisation requirements
    def test_initialisation_c(self):
        x = Calculator()
        self.assertEqual(x.register, None)
        self.assertEqual(x.operation, None)
    
    # Set_op functions
    def test_set_op_plus_c(self):    
        x.register = 0
        x.operation = None
        
        x.set_op('+')
        self.assertEqual(x.operation, '+')
        x.operation = None
     
    def test_set_op_minus_c(self):
        x.register = 0
        x.operation = None
        
        x.set_op('-')
        self.assertEqual(x.operation, '-')
        x.operation = None
        
    def test_set_op_times_c(self):   
        x.register = 0
        x.operation = None
            
        x.set_op('*')
        self.assertEqual(x.operation, '*')
        x.operation = None
        
    def test_set_op_divide_c(self):  
        x.register = 0
        x.operation = None
        
        x.set_op('/')
        self.assertEqual(x.operation, '/')
        x.operation = None
        
        
    # Set_number functions
    def test_set_number_plus_c(self):    
        x.register = None
        x.operation = None
        
        x.set_number(1)
        x.set_op('+')
        x.set_number(1)
        self.assertEqual(x.register, 2)
        x.register = None
        x.operation = None
        
    def test_set_number_minus_c(self):    
        x.register = None
        x.operation = None
        
        x.set_number(1)
        x.set_op('-')
        x.set_number(1)
        self.assertEqual(x.register, 0)
        x.register = None
        x.operation = None
        
    def test_set_number_times_c(self):    
        x.register = None
        x.operation = None
        
        x.set_number(2)
        x.set_op('*')
        x.set_number(3)
        self.assertEqual(x.register, 6)
        x.register = None
        x.operation = None
        
    def test_set_number_divide_c(self):    
        x.register = None
        x.operation = None
        
        x.set_number(6)
        x.set_op('/')
        x.set_number(2)
        self.assertEqual(x.register, 3)
        x.register = None
        x.operation = None
    
    def test_input_overflow_c(self):     
        # Input overflow
                    #Number is 99 999 999 999 999 999
        x.set_number(99999999999999999)
        self.assertEqual(x.register, 99999999999999999)
        x.set_op('+')
        x.set_number(1)
                    #Number is 100 000 000 000 000 000
        self.assertEqual(x.register, 100000000000000000)
        x.register = None
        x.operation = None
        
    def test_input_underflow_c(self):        
        # Input underflow
        # 16th digit is a 1
        x.set_number(0.00000000000001)
        self.assertEqual(x.register, 0.00000000000001)
        x.set_op('+')
        #The 1st and 17th digit is a 1
        x.set_number(1.000000000000001)
        self.assertEqual(x.register, 1.000000000000011)
        x.register = None
        x.operation = None
    
    # Clear function
    def test_clear_c(self):
        x.register = 150
        self.assertEqual(x.register, 150)
        x.clear()
        self.assertEqual(x.register, None)
        x.register = None
    
    # Evaluate function
    def test_evaluate_overflow_c(self):
        # Input overflow
        x.register = 99999999999999999
        x.operation = '+'
        p = x.evaluate(1)
        self.assertEqual(p, 100000000000000000)
        x.register = None
        x.operation = None
    def test_evaluate_underflow_c(self):    
        # Input underflow
        x.register = 0.00000000000001
        x.operation = '+'
        p = x.evaluate(1.000000000000001)
        self.assertEqual(p, 1.000000000000011)
        x.register = None
        x.operation = None
        
    ######################### NON-CRITICAL TESTS #########################
    
    ## We assume we only want '+', '-', '*', '/' as an operator, and believe
    ## deviation from that input should raise an error and handled accordingly
    
    def test_set_op_whitespace_n(self):
        x.register = 0
        x.set_op(' + ')
        self.assertEqual(x.operation, ' + ')
        x.operation = None
        x.register = None    
        
    def test_set_op_specialchars_n(self):
        x.register = 0
        x.set_op('ブレク')
        self.assertEqual(x.operation, 'ブレク')
        x.operation = None
        x.register = None
        
        x.register = 0
        x.set_op('"/^%$@#*&/,.<>|][')
        self.assertEqual(x.operation, '"/^%$@#*&/,.<>|][')
        x.operation = None
        x.register = None
        
    def test_set_op_stringOverflow_n(self):   
        x.register = 0
        
        x.set_op('a'*2049)
        self.assertEqual(x.operation, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        x.operation = None
        x.register = None
        
    def test_set_op_numberOverflow_n(self):  
        x.operation = None
        x.register = None    
        #number is 10^28
        x.set_number(10000000000000000000000000000)
        self.assertEqual(x.register, 10000000000000000000000000000)
        x.set_op('*')
        #number is 10^28
        x.set_number(10000000000000000000000000000)
        #number is 10^56
        self.assertEqual(x.register, 100000000000000000000000000000000000000000000000000000000)
        x.operation = None
        x.register = None
        
    def test_set_op_numberUnderflow_n(self):  
        x.operation = None
        x.register = None
        #number is 10^(-28)
        x.set_number(0.0000000000000000000000000001)
        self.assertEqual(x.register, 0.0000000000000000000000000001)
        x.set_op('+')
        #number is 1 + 10^(-29)
        x.set_number(1.00000000000000000000000000001)
        self.assertEqual(x.register, 1.00000000000000000000000000011)
        x.operation = None
        x.register = None
        
    # Set_number functions
    def test_set_number_string_n(self):
        x.operation = None
        x.register = None
        x.set_number('any string')
        self.assertEqual(x.register, 'any string')
        x.operation = None
        x.register = None
        
        #> Input data structures
    def test_set_number_list_n(self):
        x.operation = None
        x.register = None
        x.set_number([1,2,3])
        self.assertEqual(x.register, [1,2,3])
        x.operation = None
        x.register = None
    def test_set_number_set_n(self):
        x.operation = None
        x.register = None
        x.set_number(set([1,2,3]))
        self.assertEqual(x.register, {1,2,3})
        x.operation = None
        x.register = None
    def test_set_number_dictionary_n(self):
        x.operation = None
        x.register = None
        x.set_number({"Bob" : 16, "Jill" : 24})
        self.assertEqual(x.register, {"Bob" : 16, "Jill" : 24})
        x.operation = None
        x.register = None
    def test_set_number_tuple_n(self):
        x.operation = None
        x.register = None
        x.set_number((1,2,3))
        self.assertEqual(x.register, (1,2,3))
        x.operation = None
        x.register = None
        
    #########################> FINITE STATE MACHINE TESTING <#########################
    
    ## Here our FSM is based on the internal register state and operation of the 
    ## calculator, thus we will be checking our edges and clauses between our register 
    ## states.
    ## Calculator states include: 
    ##> (Empty Register) Register = None, Operation = None
    ##> (Register Contains Argument) Register != None, Operation = None
    ##> (Register and Operation Contains Arguments) Register != None, Operation != None
    ##> We will name these states RNA (reg no args), RCA (reg contains args), ROCA (reg,op contains args) respectively
    # We expect set_number(arg) to cause state change
    #> The state here is (register = None, operation = None)
    def RNA_set_op_edge(self):
        x.register = None
        x.operation = None
        x.set_op('+')
        self.assertEqual(x.register, None)
        self.assertEqual(x.operation, None)
        x.register = None
        x.operation = None
        
    def RNA_eval_edge(self):
        x.register = None
        x.operation = None
        x.evaluate(5)
        self.assertRaises(KeyError)
        self.assertEqual(x.register, None)
        self.assertEqual(x.operation, None)
        x.register = None
        x.operation = None
        
    def RNA_eval_edge(self):
        x.register = 5
        x.operation = '+'
        x.clear()
        self.assertEqual(x.register, None)
        self.assertEqual(x.operation, None)
        x.register = None
        x.operation = None
    
    #expected state change
    def RNA_set_number_edge(self):
        x.register = None
        x.operation = None    
        x.set_number(0)
        self.assertNotEqual(x.register, None)
        self.assertEqual(x.operation, None)
        x.register = None
        x.operation = None
    
    # We expect functions clear and set_op to cause state change
    #> The state here is (register != None, operation = None)
    # To set up state, we must use register = 0 as a default
    
    #expected state change
    def RCA_set_op_edge(self):
        x.register = 0
        x.operation = None
        
        x.set_op('+')
        self.assertNotEqual(x.register, None)
        self.assertEqual(x.operation, '+')
        x.register = 0
        x.operation = None
        
    def RCA_eval_edge(self):
        x.register = 0
        x.operation = None
        
        #x.evaluate(5)
        self.assertRaises(KeyError, x.evaluate(5))
        self.assertNotEqual(x.register, None)
        self.assertEqual(x.operation, None)
        x.register = 0
        x.operation = None
        
    #expected state change
    def RCA_clear_edge(self):
        x.register = 0
        x.operation = None
        x.clear()
        self.assertEqual(x.register, None)
        self.assertEqual(x.operation, None)
        x.register = 0
        x.operation = None
        
    def RCA_set_number_edge(self):
        x.register = 0
        x.operation = None
        
        x.set_number(5)
        self.assertNotEqual(x.register, None)
        self.assertEqual(x.operation, None)
        x.register = None
        x.operation = None
    
    # We expect functions clear and set_number to cause state change
    #> for set_number, we have multiple clauses to restrict our input space
    #> and we must prove that violating those clauses do not cause state change
    #> clauses and their tests are explained below
    #> The state here is (register != None, operation != None)
    
    # To set up state, we use register = 0 and operate = '+'
    
    def ROCA_set_op_edge(self):
        x.register = 0
        x.operation = '+'
        
        x.set_op('*')
        self.assertNotEqual(x.register, None)
        self.assertNotEqual(x.operation, None)
        x.register = 0
        x.operation = '+'
    
    def ROCA_eval_edge(self):
        x.register = 0
        x.operation = '+'    

        x.evaluate(5)
        self.assertRaises(KeyError)
        self.assertNotEqual(x.register, None)
        self.assertNotEqual(x.operation, None)
        x.register = 0
        x.operation = '+'
        
    #expected state change (reg_and_op_contains_args -> empty_reg state)
    def ROCA_clear_edge(self):
        x.register = 0
        x.operation = '+'
        
        x.clear()
        self.assertEqual(x.register, None)
        self.assertEqual(x.operation, None)
        x.register = 0
        x.operation = '+'
        
    # Set_number - expected state change (reg_and_op_contains_args -> reg_contains_arg_state)
    # We have 2 predicates that must always be fulfilled for this state change
    #> Predicate 1 (P1): Set_number is called in this state (deviation from this is proven
    #   to not lead to intended state change as shown from previous tests)
    #> Predicate 2 (P2): operation := ( ‘+’ ∨ ‘-‘∨ ‘*’ ∨ ‘/’ )
    
    #Our predicate guard states P1 ∧ P2 ∧ (P3 ∨ P4 ∨ P5 ∨ P6 ∨ P7 ∨ P8) is required for our 
    # state change
    # We will use the simplest predicates to assert their requirement
    #> Predicate 3 (P3): type(arg) := type(register) := type(int ∨ float) 
       
   # For test naming convention, we will consider n = '∧', x = not and end with T/F assertion
        
    def P1nP2nP3T(self):
        x.register = None
        x.operation = None
        ###> Assert P1 ∧ P2 ∧ P3 is T
        x.set_number(5)
        self.assertEqual(x.register, 5)
        self.assertEqual(x.operation, None)
        x.register = 0
        x.operation = '+'
    
    def P1xP2nP3F(self):
        x.register = None
        x.operation = None
        #> Assert P1 ∧ P3 ! P2 is F
        x.operation = '&'
        x.set_number(5)
        self.assertEqual(x.register, 0)
        self.assertEqual(x.operation, '&')
        x.register = 0
        x.operation = '+'
    
    def P1nP2xP3F(self):
        x.register = None
        x.operation = None    
        #> Assert P1 ∧ P2 ! P3 is F
        x.set_number([1,2,3])
        self.assertEqual(x.register, 0)
        self.assertEqual(x.operation, '+')
        x.register = 0
        x.operation = '+'
        
    # If all assertions have passed as expected, P1 and P2 predicates are required
    # for the state change we expect
    # We will now go through all predicates P1 ∧ P2 ∧ P(X)
    
    # Predicate 4: type(arg) := type(register) := type(string) ∧ operator := ‘+’ 
    
    def P1nP2nP4T(self):
        x.register = None
        x.operation = None
        ###> Assert P1 ∧ P2 ∧ P4 is T
        x.register = "Any "
        x.operation = '+'
        x.set_number("string")
        self.assertEqual(x.register, "Any string")
        self.assertEqual(x.operation, None)
        x.register = 0
        x.operation = '+'
    
    def P1nP2xP4F(self):
        x.register = None
        x.operation = None
        #> Assert P1 ∧ P2 ! P4(wrong operator) is F
        x.register = "Any "
        x.operation = '/'
        x.set_number("string")
        self.assertEqual(x.register, "Any ")
        self.assertEqual(x.operation, '/')
        x.register = 0
        x.operation = '+'
        
        # Predicate 5: (type(arg) := type(int ∨ float) ∧ (type(register) := type(string)) ∨ 
        #              (type(arg) := type(string)) ∧ (type(register) := type(int ∨ float))) ∧ 
        #              (operator := ‘*’)
        
    def P1nP2nP5T(self):
        x.register = None
        x.operation = None    
        ###> Assert P1 ∧ P2 ∧ P5 (int * string) is T
        x.register = "haha"
        x.operation = '*'
        x.set_number(3)
        self.assertEqual(x.register, "hahahahahaha")
        self.assertEqual(x.operation, None)

        x.register = None
        x.operation = None    
        #> Assert P1 ∧ P2 ∧ P5 (string * int) is T
        x.register = 3
        x.operation = '*'
        x.set_number("haha")
        self.assertEqual(x.register, "hahahahahaha")
        self.assertEqual(x.operation, None)

    def P1nP2xP5F(self):
        x.register = None
        x.operation = None        
        #> Assert P1 ∧ P2 ! P5 (int + string) is F
        x.register = 3
        x.operation = '+'
        x.set_number("haha")
        self.assertEqual(x.register, 3)
        self.assertEqual(x.operation, '+')
        
        # Predicate 6: (type(arg) := type(register) := type(set)) ∧ (operator := ‘-‘) 
        
    def P1nP2nP6T(self):
        x.register = None
        x.operation = None    
        ###> Assert P1 ∧ P2 ∧ P6 is T
        x.register = set([1,2,3])
        x.operation = '-'
        x.set_number(set([2,3,4]))
        self.assertEqual(x.register, {1})
        self.assertEqual(x.operation, None)
        
    def P1nP2xP6F(self):
        x.register = None
        x.operation = None    
        #> Assert P1 ∧ P2 ! P6(wrong operator) is F
        x.register = set([1,2,3])
        x.operation = '+'
        x.set_number(set([2,3,4]))
        self.assertEqual(x.register, {1,2,3})
        self.assertEqual(x.operation, '+')
      
        #> Assert P1 ∧ P2 ! P6(!set and set) is F
        x.register = 5
        x.operation = '-'
        x.set_number(set([1,2,3]))
        self.assertEqual(x.register, 5)
        self.assertEqual(x.operation, '-')
        
    # Predicate 7: (type(arg) := type(register) := (type(data-structure)) ∧ 
    #              (type(arg) != (type(set)∨ type(dictionary)) ∧ (operator := ‘+’) 
    
    def P1nP2nP7T(self):
        x.register = None
        x.operation = None    
        ###> Assert P1 ∧ P2 ∧ P7(tuple) is T
        x.register = (1,2,3)
        x.operation = '+'
        x.set_number((4,5,6))
        self.assertEqual(x.register, (1,2,3,4,5,6))
        self.assertEqual(x.operation, None)
        
        #> Assert P1 ∧ P2 ∧ P7(list) is T
        x.register = [1,2,3]
        x.operation = '+'
        x.set_number([4,5,6])
        self.assertEqual(x.register, [1,2,3,4,5,6])
        self.assertEqual(x.operation, None)
        
    def P1nP2xP7F(self):
        x.register = None
        x.operation = None
        #> Assert P1 ∧ P2 ! P7(wrong operator) is F
        x.register = [1,2,3]
        x.operation = '/'
        x.set_number([4,5,6])
        self.assertEqual(x.register, [1,2,3])
        self.assertEqual(x.operation, '/')
        
        #> Assert P1 ∧ P2 ! P7(wrong type) is F
        x.register = (1,2,3)
        x.operation = '+'
        x.set_number([4,5,6])
        self.assertEqual(x.register, (1,2,3))
        self.assertEqual(x.operation, '+')
        
    # Predicate 8: [(type(arg) := (type(list)∨ type(tuple)) ∧ (type(register) := type(int)) ) ∨
    #              (type(register) := (type(list)∨ type(tuple)) ∧ (type(arg) := type(int)))] ∧
    #              ((type(arg) ∧ type(register)) != (type(set)∨ type(dictionary))) ∧ (operator := '*')
    
    def P1nP2nP8T(self):
        x.register = None
        x.operation = None    
        ###> Assert P1 ∧ P2 ∧ P8(tuple) is T
        x.register = (1,2,3)
        x.operation = '+'
        x.set_number(3)
        self.assertEqual(x.register, (1,2,3,1,2,3,1,2,3))
        self.assertEqual(x.operation, None)
        
        #> Assert P1 ∧ P2 ∧ P8(list) is T
        x.register = 3
        x.operation = '*'
        x.set_number([1,2,3])
        self.assertEqual(x.register, [1,2,3,1,2,3,1,2,3])
        self.assertEqual(x.operation, None)
        
        #> Assert P1 ∧ P2 ∧ P8(list) is T
        x.register = 3
        x.operation = '*'
        x.set_number([1,2,3])
        self.assertEqual(x.register, [1,2,3,1,2,3,1,2,3])
        self.assertEqual(x.operation, None)
        
    def P1nP2xP8F(self):
        x.register = None
        x.operation = None  
        #> Assert P1 ∧ P2 ! P8(wrong operator) is F
        x.register = 3
        x.operation = '+'
        x.set_number([1,2,3])
        self.assertEqual(x.register, 3)
        self.assertEqual(x.operation, '+')
        
        #> Assert P1 ∧ P2 ! P8(wrong type) is F
        x.register = (1,2,3)
        x.operation = '*'
        x.set_number([1,2,3])
        self.assertEqual(x.register, (1,2,3))
        self.assertEqual(x.operation, '*')
    
    
if __name__ == '__main__':
    x = Calculator()
    unittest.main(exit=False)