import unittest

from src.data_structure.linked_list.doubly_ll import DoublyLL


class TestNormalCases(unittest.TestCase):
    """Testing Happy path / Normal cases on operation of dll"""

    def setUp(self):
        self.dll = DoublyLL()
        for i in [1,2,3,4]:
            self.dll.insert_at_end(i)
    
    def test_insert_at_start(self):
        self.dll.insert_at_start(5)
        self.assertEqual(self.dll.to_list(), [5,1,2,3,4])
    
    def test_insert_at_end(self):
        self.dll.insert_at_end(5)
        self.assertEqual(self.dll.to_list(), [1,2,3,4,5])
    
    def test_insert_at_pos(self):
        self.dll.insert_at_position(3,9)
        self.assertEqual(self.dll.to_list(), [1,2,9,3,4])
    
    def test_delete_at_start(self):
        self.dll.delete_at_start()
        self.assertEqual(self.dll.to_list(), [2,3,4])
    
    def test_delete_at_end(self):
        self.dll.delete_at_end()
        self.assertEqual(self.dll.to_list(), [1,2,3])
    
    def test_delete_at_pos(self):
        self.dll.delete_at_position(2)
        self.assertEqual(self.dll.to_list(), [1,3,4])
    
    def test_delete_node(self):
        self.dll.delete_node(2)
        self.assertEqual(self.dll.to_list(), [1,3,4])
    
    def test_delete_list(self):
        self.dll.delete_list()
        self.assertEqual(self.dll.to_list(), [])
    
    def test_search_node(self):
        self.assertEqual(self.dll.search_node(3), 3)
    
    def test_search_at_position(self):
        self.assertEqual(self.dll.search_at_position(3), 3)
    
    def test_reverse(self):
        self.dll.reverse()
        self.assertEqual(self.dll.to_list(), [4,3,2,1])
    
    def test_traverse_backward(self):
        self.assertEqual(self.dll.traverse_backward(), [4,3,2,1])
    
    def test_str(self):
        self.assertEqual(str(self.dll), "1 <-> 2 <-> 3 <-> 4")


class TestEdgeCases(unittest.TestCase):
    """Testing Extreme valid inputs on operations of DLL"""
    
    def test_insert_at_start_empty(self):
        self.dll = DoublyLL()
        self.dll.insert_at_start(99)
        self.assertEqual(self.dll.to_list(), [99])
    
    def test_insert_at_end_empty(self):
        self.dll = DoublyLL()
        self.dll.insert_at_end(99)
        self.assertEqual(self.dll.to_list(), [99])
    
    def test_insert_at_pos_start(self):
        self.dll = DoublyLL()
        for i in range(1,5):
            self.dll.insert_at_end(i)
        self.dll.insert_at_position(1,7)
        self.assertEqual(self.dll.to_list(), [7,1,2,3,4])
    
    def test_insert_at_pos_end(self):
        self.dll = DoublyLL()
        for i in range(1,5):
            self.dll.insert_at_end(i)
        self.dll.insert_at_position(5,7)
        self.assertEqual(self.dll.to_list(), [1,2,3,4,7])
    
    def test_insert_at_pos_one_empty(self):
        self.dll = DoublyLL()
        self.dll.insert_at_position(1,99)
        self.assertEqual(self.dll.to_list(), [99])
    
    def test_delete_at_start_one(self):
        self.dll = DoublyLL()
        self.dll.insert_at_end(1)
        self.dll.delete_at_start()
        self.assertEqual(self.dll.to_list(), [])
    
    def test_delete_at_end_one(self):
        self.dll = DoublyLL()
        self.dll.insert_at_end(1)
        self.dll.delete_at_end()
        self.assertEqual(self.dll.to_list(), [])
    
    def test_delete_at_pos_one(self):
        self.dll = DoublyLL()
        self.dll.insert_at_end(1)
        self.dll.delete_at_position(1)
        self.assertEqual(self.dll.to_list(), [])
    
    def test_delete_at_pos_start(self):
        self.dll = DoublyLL()
        for i in range(1,5):
            self.dll.insert_at_end(i)
        self.dll.delete_at_position(1)
        self.assertEqual(self.dll.to_list(), [2,3,4])
    
    def test_delete_at_pos_end(self):
        self.dll = DoublyLL()
        for i in range(1,5):
            self.dll.insert_at_end(i)
        self.dll.delete_at_position(4)
        self.assertEqual(self.dll.to_list(), [1,2,3])
    
    def test_delete_node_one(self):
        self.dll = DoublyLL()
        self.dll.insert_at_end(1)
        self.dll.delete_node(1)
        self.assertEqual(self.dll.to_list(), [])
    
    def test_delete_node_start(self):
        self.dll = DoublyLL()
        for i in range(1,5):
            self.dll.insert_at_end(i)
        self.dll.delete_node(1)
        self.assertEqual(self.dll.to_list(), [2,3,4])
    
    def test_delete_node_end(self):
        self.dll = DoublyLL()
        for i in range(1,5):
            self.dll.insert_at_end(i)
        self.dll.delete_node(4)
        self.assertEqual(self.dll.to_list(), [1,2,3])
    
    def test_delete_list_one(self):
        self.dll = DoublyLL()
        self.dll.insert_at_end(1)
        self.dll.delete_list()
        self.assertEqual(self.dll.to_list(), [])
    
    def test_reverse_one(self):
        self.dll = DoublyLL()
        self.dll.insert_at_end(1)
        self.dll.reverse()
        self.assertEqual(self.dll.to_list(), [1])
    
    def test_reverse_empty(self):
        self.dll = DoublyLL()
        self.dll.reverse()
        self.assertEqual(self.dll.to_list(), [])
    
    def test_traverse_backward_one(self):
        self.dll = DoublyLL()
        self.dll.insert_at_end(4)
        self.assertEqual(self.dll.traverse_backward(), [4])
    
    def test_traverse_backward_empty(self):
        self.dll = DoublyLL()
        self.assertEqual(self.dll.traverse_backward(), [])


class TestFailCases(unittest.TestCase):
    """Testing invalid inputs or fail cases on operations of DLL"""
    def setUp(self):
        self.dll = DoublyLL()
        for i in range(1,5):
            self.dll.insert_at_end(i)
    
    def test_insert_at_position_invalid_type(self):
        with self.assertRaises(TypeError):
            self.dll.insert_at_position(3.4, 30)
    
    def test_insert_at_position_less_than_one(self):
        with self.assertRaises(IndexError):
            self.dll.insert_at_position(-2, 20)

    
    def test_insert_at_position_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.dll.insert_at_position(6, 21)
    
    def test_insert_at_position_empty_invalid(self):
        self.dll.delete_list()
        with self.assertRaises(ValueError):
            self.dll.insert_at_position(2,4)
    
    def test_delete_at_start_empty(self):
        self.dll.delete_list()
        with self.assertRaises(ValueError):
            self.dll.delete_at_start()
    
    def test_delete_at_end_empty(self):
        self.dll.delete_list()
        with self.assertRaises(ValueError):
            self.dll.delete_at_end()
    
    def test_delete_at_position_empty(self):
        self.dll.delete_list()
        with self.assertRaises(ValueError):
            self.dll.delete_at_position(1)
    
    def test_delete_at_position_invalid_type(self):
        with self.assertRaises(TypeError):
            self.dll.delete_at_position(3.5)
    
    def test_delete_at_position_lower_bound(self):
        with self.assertRaises(IndexError):
            self.dll.delete_at_position(-1)
    
    def test_delete_at_position_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.dll.delete_at_position(6)
    
    def test_delete_node_empty(self):
        self.dll.delete_list()
        with self.assertRaises(ValueError):
            self.dll.delete_node(1)
    
    def test_delete_node_not_found(self):
        with self.assertRaises(ValueError):
            self.dll.delete_node(5)
    
    def test_delete_list_empty(self):
        self.dll.delete_list()
        with self.assertRaises(ValueError):
            self.dll.delete_list()
    
    def test_search_node_empty(self):
        self.dll.delete_list()
        with self.assertRaises(ValueError):
            self.dll.search_node(2)
    
    def test_search_node_not_found(self):
        with self.assertRaises(ValueError):
            self.dll.search_node(6)
    
    def test_search_at_position_invalid_type(self):
        with self.assertRaises(TypeError):
            self.dll.search_at_position(3.7)
    
    def test_search_at_position_lower_bound(self):
        with self.assertRaises(IndexError):
            self.dll.search_at_position(0)
    
    def test_search_at_position_empty(self):
        self.dll.delete_list()
        with self.assertRaises(ValueError):
            self.dll.search_at_position(1)
    
    def test_search_at_position_out_of_bound(self):
        with self.assertRaises(IndexError):
            self.dll.search_at_position(6)


