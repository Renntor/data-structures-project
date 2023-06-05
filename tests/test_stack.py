"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class TestNodeStack(unittest.TestCase):


    def test_node(self):
        """Тест Node"""
        tests_node = Node(1, None)
        first_item = Node('data1', tests_node)
        self.assertEqual(first_item.data, 'data1')
        self.assertEqual(first_item.next_node, tests_node)


    def test_stack(self):
        """Тест Stack"""
        stack = Stack()
        self.assertEqual(stack.top, None)
        stack.push('data1')
        stack.push('data2')
        self.assertEqual(isinstance(stack.top, Node), True)
        self.assertEqual(stack.pop(), 'data2')
        self.assertEqual(stack.pop(), 'data1')
        self.assertEqual(stack.pop(), None)
        stack.push('data1')
        self.assertEqual(str(stack), "data1")
