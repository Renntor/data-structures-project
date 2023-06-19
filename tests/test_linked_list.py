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
        self.assertEqual(str(ll), "{'name': 'Misha'} -> {'name': 'Oleg'} -> {'name': 'Anna'} -> {'name': 'Anya'} -> None")

