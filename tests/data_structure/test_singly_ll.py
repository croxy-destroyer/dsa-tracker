import unittest

from src.data_structure.linked_list.singly_ll import SinglyLL


class TestNormalCase(unittest.TestCase):

    def setUp(self):
        self.sll = SinglyLL()
        for i in [10, 20, 30]:
            self.sll.insert_at_end(i)

    def test_insert_at_start(self):
        self.sll.insert_at_start(5)
        self.assertEqual(self.sll.to_list(), [5, 10, 20, 30])

    def test_insert_at_end(self):
        self.sll.insert_at_end(21)
        self.assertEqual(self.sll.to_list(), [10, 20, 30, 21])

    def test_insert_at_pos(self):
        self.sll.insert_at_postion(2, 22)
        self.assertEqual(self.sll.to_list(), [10, 22, 20, 30])

    def test_delete_at_start(self):
        self.sll.delete_at_start()
        self.assertEqual(self.sll.to_list(), [20, 30])

    def test_delete_list(self):
        self.sll.delete_list()
        self.assertEqual(self.sll.to_list(), [])

    def test_delete_end(self):
        self.sll.delete_at_end()
        self.assertEqual(self.sll.to_list(), [10, 20])

    def test_delete_at_pos(self):
        self.sll.delete_at_position(2)
        self.assertEqual(self.sll.to_list(), [10, 30])

    def test_delete_node(self):
        self.sll.delete_node(20)
        self.assertEqual(self.sll.to_list(), [10, 30])

    def test_str(self):
        self.assertEqual(str(self.sll), "10 -> 20 -> 30")

    def test_length(self):
        self.assertEqual(self.sll.length_sll(), 3)

    def test_search_pos(self):
        self.assertEqual(self.sll.search_at_pos(2), 20)

    def test_search_node(self):
        self.assertEqual(self.sll.search_node(30), 3)

    def test_reverse(self):
        self.sll.reverse()
        self.assertEqual(self.sll.to_list(), [30, 20, 10])



class TestEdgeCases(unittest.TestCase):
    
    def test_insert_start_empty_list(self):
        self.sll = SinglyLL()
        self.sll.insert_at_start(1)
        self.assertEqual(self.sll.to_list(), [1])

    def test_insert_end_empty_list(self):
        self.sll = SinglyLL()
        self.sll.insert_at_end(1)
        self.assertEqual(self.sll.to_list(), [1])

    def test_insert_pos_at_start(self):
        self.sll = SinglyLL()
        self.sll.insert_at_postion(1, 100)
        self.sll.insert_at_postion(1, 10)
        self.assertEqual(self.sll.to_list(), [10, 100])

    def test_insert_pos_end(self):
        self.sll = SinglyLL()
        self.sll.insert_at_end(2)
        self.sll.insert_at_end(3)
        self.sll.insert_at_postion(2, 2.5)
        self.sll.insert_at_postion(4, 4.5)
        self.assertEqual(self.sll.to_list(), [2, 2.5, 3, 4.5])

    def test_insert_pos1_empty(self):
        self.sll = SinglyLL()
        self.sll.insert_at_postion(1, 2.9)
        self.assertEqual(self.sll.to_list(), [2.9])

    def test_delete_start_if_one_element(self):
        self.sll = SinglyLL()
        self.sll.insert_at_end(1)
        self.sll.delete_at_start()
        self.assertEqual(self.sll.to_list(), [])

    def test_delete_end_one_element(self):
        self.sll = SinglyLL()
        self.sll.insert_at_end(2)
        self.sll.delete_at_end()
        self.assertEqual(self.sll.to_list(), [])

    def test_delete_pos1_one_element(self):
        self.sll = SinglyLL()
        self.sll.insert_at_end(1)
        self.sll.delete_at_position(1)
        self.assertEqual(self.sll.to_list(), [])

    def test_delete_node_at_start(self):
        self.sll = SinglyLL()
        self.sll.insert_at_end(1)
        self.sll.insert_at_end(2)
        self.sll.delete_node(1)
        self.assertEqual(self.sll.to_list(), [2])

    def test_delete_node_start_one_element(self):
        self.sll = SinglyLL()
        self.sll.insert_at_end(1)
        self.sll.delete_node(1)
        self.assertEqual(self.sll.to_list(), [])

    def test_str_empthy(self):
        self.sll = SinglyLL()
        self.assertEqual(str(self.sll), "")

    def test_reverse_empty(self):
        self.sll = SinglyLL()
        self.sll.reverse()
        self.assertEqual(self.sll.to_list(), [])

    def test_reverse_one_element(self):
        self.sll = SinglyLL()
        self.sll.insert_at_end(1)
        self.assertEqual(self.sll.to_list(), [1])


class TestFailCases(unittest.TestCase):

    def setUp(self):
        self.sll = SinglyLL()
        for i in [1, 2, 3,4]:
            self.sll.insert_at_end(i)

    def test_insert_posinvalid_type(self):
        with self.assertRaises(TypeError):
            self.sll.insert_at_postion("first", 20)

    def test_insert_pos_less_than1(self):
        with self.assertRaises(IndexError):
            self.sll.insert_at_postion(-1, 3)

    def test_insert_pos_out_of_bound(self):
        with self.assertRaises(IndexError):
            self.sll.insert_at_postion(6, 67)

    def test_insert_pos_not1_empty(self):
        self.sll.delete_list()
        with self.assertRaises(ValueError):
            self.sll.insert_at_postion(3, 20)

    def test_delete_empty(self):
        self.sll.delete_list()
        with self.assertRaises(ValueError):
            self.sll.delete_list()

    def test_delete_start_empty(self):
        self.sll.delete_list()
        with self.assertRaises(ValueError):
            self.sll.delete_at_start()

    def test_delete_end_empty(self):
        self.sll.delete_list()
        with self.assertRaises(ValueError):
            self.sll.delete_at_end()

    def test_delete_pos_empty(self):
        self.sll.delete_list()
        with self.assertRaises(ValueError):
            self.sll.delete_at_position(3)

    def test_delete_node_empty(self):
        self.sll.delete_list()
        with self.assertRaises(ValueError):
            self.sll.delete_node(2)

    def test_delete_pos_invalid_type(self):
        with self.assertRaises(TypeError):
            self.sll.delete_at_position(3.4)

    def test_delete_pos_less_than1(self):
        with self.assertRaises(IndexError):
            self.sll.delete_at_position(-4)

    def test_delete_pos_out_of_bound(self):
        with self.assertRaises(IndexError):
            self.sll.delete_at_position(5)

    def test_delete_node_not_found(self):
        with self.assertRaises(ValueError):
            self.sll.delete_node(25)

    def test_search_pos_invalid_type(self):
        with self.assertRaises(TypeError):
            self.sll.search_at_pos(2.3)

    def test_search_pos_less_than1(self):
        with self.assertRaises(IndexError):
            self.sll.search_at_pos(-3)

    def test_search_pos_out_of_bound(self):
        with self.assertRaises(IndexError):
            self.sll.search_at_pos(12)

    def test_search_pos_empty(self):
        self.sll.delete_list()
        with self.assertRaises(ValueError):
            self.sll.search_at_pos(1)

    def test_search_node_empty(self):
        self.sll.delete_list()
        with self.assertRaises(ValueError):
            self.sll.search_node(3)

    def test_search_node_value_not_found(self):
        with self.assertRaises(ValueError):
            self.sll.search_node(23)
