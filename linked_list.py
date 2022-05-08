
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def to_array(self):
        array = []
        if self.head is None:
            return array

        node = self.head
        while node:
            array.append(node.data)
            node = node.next_node

        return array

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)

        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node

    def get_user_by_id(self, user_id):
        node = self.head

        while node:
            if node.data["id"] == int(user_id):
                return node.data
            node = node.next_node
        return None

    def print_ll(self):
        ll_string = ""
        node = self.head
        if node is None:
            print("")
        while node:
            ll_string += f"{str(node.data)} ->" if node.next_node is not None else "None"
            node = node.next_node
        print(ll_string)

ll = LinkedList()
node4 = Node("4th node", None)
node3 = Node("3rd node", node4)
node2 = Node("2nd node", node3)
node1 = Node("1st node", node2)

ll.head = node1
ll.print_ll()
