'''测试ChapterTwoExercises.py'''
import unittest

from unittest import mock

from ChapterTwoExercises import *

import HTMLTestRunner


class TestChapterTwoExercises(unittest.TestCase):
    '''测试 TxtHandle'''
    def setUp(self):
        self.txt_handle = TxtHandle('D:\桌面\eng2.txt', 'D:\桌面\query.txt')

    def test_init_query_file(self):
        self.assertRaises(TypeError, TxtHandle, (1,'D:\桌面\query.txt'))
        self.assertRaises(TypeError, TxtHandle, ('D:\桌面\eng2.txt',2))
    
    def test_file_analysis(self):
        self.txt_handle.file_analysis()
        

    
   

def main():
    filepath = 'F:/multisim/VsCode/软件工程学习/英文检索单元测试、覆盖率测试/test_ChapterTwoEx.html'
    ftp=open(filepath,'wb')

    suite = unittest.makeSuite(TestChapterTwoExercises)
    
    # unittest.main(verbosity=2)
    runner=HTMLTestRunner.HTMLTestRunner(stream=ftp,title='test_ChapterTwoEx')
    runner.run(suite)
    
if __name__ == '__main__':
    
    main()
    
    
    