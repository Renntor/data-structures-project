"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Node, Queue


class TestNodeQueue(unittest.TestCase):

    def test_node(self):
        """Тест Node"""
        tests_node = Node('data1', None)
        self.assertEqual(repr(tests_node), "Node('data1',None)")
        self.assertEqual(str(tests_node), 'data1')
        first_item = Node('data2', tests_node)
        self.assertEqual(first_item.data, 'data2')
        self.assertEqual(first_item.next_node.data, 'data1')


    def test_queue(self):
        """Тест Queue"""
        queue = Queue()
        self.assertEqual(queue.all_data, '')
        self.assertEqual(repr(queue), "Queue(None,None)")
        queue.enqueue('data1')
        queue.enqueue('data2')
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(str(queue), 'data1\ndata2')
        self.assertEqual(queue.tail.data, 'data2')
        queue.enqueue('data3')
        self.assertEqual(queue.tail.data, 'data3')

        # Test dequeue
        self.assertEqual(queue.dequeue(), 'data1')
        queue.dequeue()
        queue.dequeue()
        self.assertIs(queue.dequeue(), None)
