class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data: dict, next_node=None) -> None:
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""
    head = None
    tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        node = Node(data, self.tail)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            next_head = self.head
            self.head = node
            self.head.next_node = next_head

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        node = Node(data)
        self.tail.next_node = node
        self.tail = node



    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string
