"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import *
class TestNodeLink(unittest.TestCase):
    def test_Node(self):
        """Test Node"""
        node = Node({'name': "Oleg"})
        self.assertEqual(node.data, {'name': 'Oleg'})
        self.assertEqual(node.next_node, None)


    def test_Link(self):
        ll = LinkedList()
        self.assertEqual(str(ll), 'None')
        ll.insert_beginning({'name': 'Oleg'})
        ll.insert_beginning({'name': 'Misha'})
        ll.insert_at_end({'name': "Anna"})
        ll.insert_at_end({'name': 'Anya'})
        self.assertEqual(str(ll), "{'name': 'Misha'} -> {'name': 'Oleg'} -> {'name': 'Anna'} -> "
                                  "{'name': 'Anya'} -> None")


    def test_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({'name': 'Oleg'})
        ll.insert_at_end({'name': "Anna"})
        self.assertEqual(ll.to_list(), [{'name': 'Oleg'}, {'name': "Anna"}])

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 0})
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end('0')
        self.assertEqual(ll.get_data_by_id(1), {'id': 1})
        self.assertEqual(ll.get_data_by_id(5), None)