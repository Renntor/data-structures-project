class Node:
    """Класс для узла очереди"""

    def __init__(self, data: str, next_node=None) -> None:
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.data}',{self.next_node})"

    def __str__(self):
        return f"{self.data}"


class Queue:
    """Класс для очереди"""

    def __init__(self) -> None:
        """Конструктор класса Queue"""
        self.all_data = ''
        self.head = None
        self.tail = None

    def __repr__(self):
        return f"{self.__class__.__name__}({self.head},{self.tail})"

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        return self.all_data


    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.all_data = self.head.data
        else:
            self.tail.next_node = new_node
            self.tail = new_node
            self.all_data += '\n' + self.tail.data

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        else:
            remote = self.head
            self.head = self.head.next_node
            return remote.data

