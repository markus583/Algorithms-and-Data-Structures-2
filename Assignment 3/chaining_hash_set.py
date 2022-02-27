"""Implement hash table using overflow chains."""
from chaining_hash_node import ChainingHashNode


class ChainingHashSet:
    """Class implementing hashing and chaining for a set."""

    def __init__(self, capacity: int = 0) -> None:
        """Initialize a new hash table with a given capacity.

        :param capacity: how many elements the hash table shall be able to store.
        :return: None
        :raises: ValueError if the capacity is negative or if capacity is not an int.
        """
        if not isinstance(capacity, int):
            raise ValueError("capacity must be an int")
        if capacity < 0:
            raise ValueError("capacity must not be negative")

        self.hash_table = [None] * capacity
        self.table_size = 0
        self.capacity = capacity

    def get_hash_code(self, key: int) -> int:
        """Hash function calculating a hash code for a given key using modulo division.

        :param key: Key for which a hash code shall be calculated according to the length of the hash table.
        :return: The calculated hash code for the given key.
        """
        return key % self.capacity

    def get_hash_table(self) -> list:
        """Return the hash table.

        (Required for testing only)
        :return the hash table.
        """
        return self.hash_table

    def set_hash_table(self, table: list) -> None:
        """Set a given hash table.

        :param table: Given hash table which shall be used.
        !!!
        (Required for testing only)
        Since this method is needed for testing we decided to implement it.
        You do not need to change or add anything.
        !!!
        """
        self.hash_table = table
        self.capacity = len(table)
        self.table_size = 0
        for node in table:
            while node is not None:
                self.table_size += 1
                node = node.next

    def get_table_size(self) -> int:
        """Return the number of stored keys (keys must be unique!)."""
        return self.table_size

    def insert(self, key: int) -> bool:
        """Insert a key and return True if it was successful.

        :param key: The key which shall be stored in the hash table.
        :return: True if key could be inserted, or False if the key is already in the hash table.
        :raises: ValueError if any of the input parameters is None.
        """
        if key is None:
            raise ValueError("key must not be None")
        hash_value: int = self.get_hash_code(key)
        node = self.hash_table[hash_value]
        if node is None:  # vacant slot
            self.hash_table[hash_value] = ChainingHashNode(key)
        else:
            while node is not None:
                if node.key == key:  # key already in hash table
                    return False
                previous_node = node
                node = node.next
            previous_node.next = ChainingHashNode(
                key
            )  # insert new node at end of chain

        self.table_size += 1
        return True

    def contains(self, key: int):
        """Search for a given key in the hash table.

        :param key: The key to be searched in the hash table.
        :return: True if the key is already stored, otherwise False.
        :raises: a ValueError if the key is None.
        """
        if key is None:
            raise ValueError("key must not be None")

        hash_value = self.get_hash_code(key)
        node = self.hash_table[hash_value]
        while node is not None:
            if node.key == key:
                return True
            node = node.next
        return False

    def remove(self, key):
        """Remove the key from the hash table and return True on success, False otherwise.

        :param key: The key to be removed from the hash table.
        :return: True if the key was found and removed, False otherwise.
        :raises: ValueError if the key is None.
        """
        if key is None:
            raise ValueError("key must not be None")

        hash_value = self.get_hash_code(key)
        node = self.hash_table[hash_value]
        previous_node = None

        while node is not None:
            if node.key == key:
                if previous_node is None:  # currently 1 node in chain
                    self.hash_table[hash_value] = node.next
                else:
                    previous_node.next = node.next  # cut out node
                self.table_size -= 1
                return True
            previous_node = node
            node = node.next
        return False  # key never found

    def clear(self) -> None:
        """Remove all stored elements from the hash table by setting all nodes to None."""
        self.hash_table = [None] * self.capacity
        self.table_size = 0

    def to_string(self) -> str:
        """Return a string representation of the hash table (array indices and stored keys).

        In the format
        Idx_0 {Node, Node, ... }, Idx_1 {...}
        e.g.: 0 {13}, 1 {82, 92, 12}, 2 {2, 32},
        """
        result = ""
        for i in range(self.capacity):
            result += str(i) + " {"
            node = self.hash_table[i]
            while node is not None:
                result += str(node.key)
                node = node.next
                if node is not None:
                    result += ", "
            result += "}, "
        return result
