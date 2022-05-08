class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def custom_hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
            hash_value = (hash_value * ord(char)) % self.table_size
        return hash_value

    def add_key_value(self, key, value):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:
            self.hash_table[hashed_key] = Node(Data(key, value), None)
        else:
            node = self.hash_table[hashed_key]
            while node.next_node:
                node = node.next_node
            node.next_node = Node(Data(key, value), None)

    def get_value(self, key):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is not None:
            node = self.hash_table[hashed_key]
            if node.next_node is None:
                return node.data.value
            while node.next_node:
                if key == node.data.key:
                    return node.data.value
                node = node.next_node

            return node.data.value if key == node.data.key else None

    def print_table(self):
        print("{")
        for index, value in enumerate(self.hash_table):
            if value is not None:
                ll_string = ""
                node = value
                if node.next_node:
                    while node.next_node:
                        ll_string += (
                            str(node.data.key) + " : " + str(node.data.value) + " -> "
                        )
                        node = node.next_node
                    ll_string += (
                            str(node.data.key) + " : " + str(node.data.value) + " -> None "
                        )
                    print(f"[{index}] {ll_string}")
                else:
                    print(f"[{value.data.key}] : {value.data.value}")
            else:
                print(f"[{index}] {value}")
        print("}")

hash_table = HashTable(4)
hash_table.add_key_value("test_key", "test_value")
hash_table.add_key_value("test_key", "test_value")
hash_table.print_table()
