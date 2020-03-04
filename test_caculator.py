'''test 计算器.py'''
import unittest

from 计算器 import *

class TestCaculator(unittest.TestCase):
    '''test 计算器'''
    def test_conversionFormula(self):
        '''test method conversionFormula'''
        self.assertEqual(['1', '+', '(', '2', '+', '3', ')'], conversionFormula('1+(2+3)'))
        self.assertEqual(['1', '+', '2', '*', '3'], conversionFormula('1+2*3'))
        self.assertEqual('ERROR', conversionFormula('1(2,3)'))
        self.assertEqual('ERROR', conversionFormula('1,2,3'))
        self.assertEqual('ERROR', conversionFormula('1*(2++3)'))
        self.assertEqual('ERROR', conversionFormula('1*(2/0)'))
        self.assertEqual('ERROR', conversionFormula('a*(2+3)'))
        self.assertEqual('ERROR', conversionFormula('1/(2+3))'))
        self.assertEqual('ERROR', conversionFormula('!&@'))
        self.assertEqual('ERROR', conversionFormula('*2'))
        self.assertEqual
    def test_calculator(self):
        '''test method calculator'''
        self.assertEqual(27,calculator(['2','^','3','*','2','+','13','-','4','/','2']))
        self.assertEqual(3,calculator(['-','2','^','2','*','2','+','13','-','4','/','2']))
        self.assertEqual(1,calculator(['+','1']))
        self.assertEqual('ERROR',calculator(['*','2']))
    def test_remove_racket(self):
        '''test method remove_racket'''
        self.assertEqual(['7.0'], remove_bracket(['-','(','2','-','3','*','(','1','+','2',')',')']))

if __name__ == '__main__':
    unittest.main(verbosity=2)
