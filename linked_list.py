class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def print_ll(self):
        current = self.head
        items = []
        while current:
            items.append(str(current.data))
            current = current.next
        print(" -> ".join(items) if items else "Пустой список")

    def print_ll_from_tail(self):
        current = self.head
        items = []
        while current:
            items.append(str(current.data))
            current = current.next
        items.reverse()
        print(" <- ".join(items) if items else "Пустой список")

    def insert_at_index(self, index, data):
        if index <= 0:
            # Вставка в начало
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            if not self.tail:
                self.tail = new_node
            return True

        current = self.head
        current_index = 0
        while current and current_index < index - 1:
            current = current.next
            current_index += 1

        if current:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
            if current == self.tail:
                self.tail = new_node
            return True

        self.append(data)
        return True

    def remove_node_data(self, data):
        if not self.head:
            return False

        if self.head.data == data:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return True

        current = self.head
        while current.next:
            if current.next.data == data:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                return True
            current = current.next

        return False

    def len_ll(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def contains_from_head(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def contains_from_tail(self, data):
        return self.contains_from_head(data)
    def contains_from(self, data, from_head=True):
        if from_head:
            return self.contains_from_head(data)
        return self.contains_from_tail(data)