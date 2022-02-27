"""Initialize a base class to chain hash nodes."""


class ChainingHashNode:
    """Implement a node for a chaining hash table."""

    def __init__(self, key: int = None) -> None:
        """
        Initialize a new node.

        :param key: key of the node.
        :return: None
        """
        self.key = key
        self.next = None
