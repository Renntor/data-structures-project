"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class Teststack(unittest.TestCase):

    def test_node(self):
        """Тест Node"""
        first = Node(5, None)
        self.assertEqual(first.data, 5)
        self.assertEqual(first.next_node, None)

    def test_stack(self):
        """Тест Stack"""
        second = Stack()
        self.assertEqual(second.top, None)
        second.push('data1')
        self.assertEqual(isinstance(second.top, Node), True)
        self.assertEqual(second.pop(), 'data1')
        self.assertEqual(second.pop(), None)
