'''test 计算器.py'''
import unittest

from 计算器 import *

import HTMLTestRunner

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
        self.assertEqual('ERROR', conversionFormula(''))
        self.assertEqual('ERROR', conversionFormula('123'))
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
        self.assertEqual(['1', '-', '7.0'], remove_bracket(['1','+','(','2','-','3','*','(','1','+','2',')',')']))
        self.assertEqual(['-','5.0'], remove_bracket(['-','(','2','-','3','*','(','1','-','2',')',')']))
def main():
    filepath = 'F:/multisim/VsCode/软件工程学习/计算器单元测试、覆盖率测试/test_calculator_report.html'
    
    ftp=open(filepath,'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestCaculator('test_conversionFormula'))
    suite.addTest(TestCaculator('test_calculator'))
    suite.addTest(TestCaculator('test_remove_racket'))
    runner=HTMLTestRunner.HTMLTestRunner(stream=ftp,title='test_caculator')
    runner.run(suite)
    
if __name__ == '__main__':
    main()
	
    # unittest.main(verbosity=2)