class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.all_data = ''
        self.head = None
        self.tail = None


    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if self.all_data == '':
            self.head = Node(data, None)
            self.all_data += self.head.data
        elif self.head.next_node == None:
            self.tail = Node(data, None)
            self.head.next_node = self.tail
            self.all_data += '\n' + self.tail.data
        else:
            tail = Node(data, None)
            self.tail.next_node = tail
            self.tail = tail
            self.all_data += '\n' + self.tail.data


    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        return self.all_data

