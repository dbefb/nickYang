'''测试game_map.py'''
import unittest

from unittest import mock
from game_map import *

import HTMLTestRunner

from itertools import cycle

class TestGameMap(unittest.TestCase):
    '''测试 GameMap'''
    def setUp(self):
        self.game_map = GameMap(5, 4)

    def test_init(self):
        self.assertRaises(TypeError, GameMap,(1.2,3))
        self.assertRaises(TypeError, GameMap,(3,1.3))

    def test_rows(self):
        self.assertEqual(5,self.game_map.rows)
        self.assertEqual(4,self.game_map.cols)

    @mock.patch('random.random', new = mock.Mock(side_effect = cycle([0.4, 0.6])))
    def test_reset_get_set(self):
        
        self.game_map.reset()
        self.assertEqual([[1,0,1,0],[1,0,1,0],[1,0,1,0],[1,0,1,0],[1,0,1,0]], self.game_map.cells)
        self.assertEqual(1, self.game_map.get(0,0))
        self.assertRaises(TypeError,self.game_map.get,(1.2,2))
        self.assertRaises(TypeError,self.game_map.get,(2,1.2))
        self.game_map.set(0,0,0)
        self.assertEqual(0, self.game_map.get(0,0))
        self.assertRaises(TypeError,self.game_map.set,(6,0,0))
        self.assertRaises(TypeError,self.game_map.set,(0,4,0))
        self.assertRaises(TypeError,self.game_map.set,(0,0,2))
    @mock.patch('random.random', new = mock.Mock(side_effect = cycle([0.4])))
    def test_get_neighbor_count_and_map(self):
        self.game_map.reset()
        for i in range(0,self.game_map.rows):
            for j in range(0,self.game_map.cols):
                self.assertEqual(8, self.game_map.get_neighbor_count(i,j))
        self.assertEqual([[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8]], self.game_map.get_neighbor_count_map())
        self.assertRaises(TypeError,self.game_map.get_neighbor_count,(5,0))
        self.assertRaises(TypeError,self.game_map.get_neighbor_count,(0,5))

    def test_set_map(self):
        self.game_map.set_map([[0,0,0,0],[1,1,1,1],[0,1,0,1],[1,0,1,0],[1,1,0,0]])
        self.assertEqual([[0,0,0,0],[1,1,1,1],[0,1,0,1],[1,0,1,0],[1,1,0,0]], self.game_map.cells)
        self.assertRaises(TypeError,self.game_map.set_map,(5))
        self.assertRaises(AssertionError,self.game_map.set_map,([[0]*4]*4))
        self.assertRaises(TypeError,self.game_map.set_map,([0]*5))
        self.assertRaises(AssertionError,self.game_map.set_map,([[0]*3]*4))
        self.assertRaises(TypeError,self.game_map.set_map,([[0.1]*4]*5))
        self.assertRaises(AssertionError,self.game_map.set_map,([[2]*4]*5))
    
    def test_print_map(self):
        self.assertRaises(TypeError,self.game_map.print_map,(1))
        self.assertRaises(TypeError,self.game_map.print_map,([1,2],1))
        self.game_map.print_map = mock.Mock()
        self.game_map.print_map(['2'])
        self.game_map.print_map.assert_called_with(['2'])
        
    def main():     
        suite = unittest.makeSuite(TestGameMap)
            # unittest.main(verbosity=2)     
        runner = unittest.TextTestRunner()     
        runner.run(suite) 
if __name__ == '__main__':

    main()