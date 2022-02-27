"""
Implements an AVL tree.
"""
from typing import Generator, Iterator, Union, Any, Tuple
from copy import deepcopy
from collections import defaultdict

from avl_node import AVLNode


class AVLTree:
    """
    AVL Tree implementation.
    """

    def __init__(self) -> None:
        """Default constructor. Initializes the AVL tree."""
        self.root = None
        self.size = 0

    def get_tree_root(self) -> Union[None, AVLNode]:
        """
        Method to get the root node of the AVLTree
        :return AVLNode -- the root node of the AVL tree
        """
        if self.root:
            return self.root
        return None

    def get_tree_height(self) -> int:
        """Retrieves tree height.
        :return -1 in case of empty tree, current tree height otherwise.
        """
        return self.get_height(self.root)

    def get_tree_size(self) -> int:
        """Yields number of key/value pairs in the tree.
        :return Number of key/value pairs.
        """
        return self.size

    def to_array(self) -> list:
        """Yields an array representation of the tree's values (pre-order).
        :return Array representation of the tree values.
        """
        array = list(self.preorder())
        for i, value in enumerate(array):  # only return key values, not entire node
            array[i] = value.value
        return array

    def update_heights(self, node: AVLNode) -> None:
        """Updates the heights of all nodes in the tree."""
        parent = node.parent
        while parent:
            parent.height = self._update_single_height(parent)
            parent = parent.parent

    def find_by_key(
        self, key, _return_node=False
    ) -> Union[Union[int, float], AVLNode, None]:
        """Returns value of node with given key.
        :param _return_node: whether to return node or key.
        :param key: Key to search.
        :return Corresponding value if key was found, None otherwise.
        :raises ValueError if the key is None
        """
        current = self.root
        while current:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:  # equality --> key found
                if _return_node:
                    return current
                return current.key
        return None

    def insert(self, key: Union[int, float], value: Any) -> bool:
        """Inserts a new node into AVL tree.
        :param key: Key of the new node.
        :param value: Data of the new node. May be None. Nodes with the same key
        are not allowed. In this case False is returned. None-Keys and None-Values are
        not allowed. In this case an error is raised.
        :return True if the insert was successful, False otherwise.
        :raises ValueError if the key or value is None.
        """
        if key is None:
            raise ValueError("Key cannot be None.")
        if value is None:
            raise ValueError("Value cannot be None.")

        new = AVLNode(key=key, value=value)  # create new node
        parent = None  # parent of new node
        current = self.root
        while current:  # find the right place for the new node
            parent = current  # set parent to current node
            if new.key < current.key:  # go left
                current = current.left
            elif new.key > current.key:  # go right
                current = current.right
            else:  # duplicate key
                return False

        new.parent = parent  # set parent of new node
        if parent is None:  # tree is empty
            self.root = new  # set root to new node
        else:
            if new.key < parent.key:
                parent.left = new
            else:
                parent.right = new

            # fix tree
            # if parent had 1 child before, tree is still balanced
            # else: rebalance the tree
            if not (parent.left and parent.right):
                self._cut_link_restructuring(new)
        self.size += 1
        return True

    def remove_by_key(self, key: int) -> bool:
        """Removes node with given key.
        :param key: Key of node to remove.
        :return True If node was found and deleted, False otherwise.
        @raises ValueError if the key is None.
        """
        if key is None:
            raise ValueError("Key cannot be None.")

        node_to_remove = self.find_by_key(key=key, _return_node=True)
        # tree consists of only one node
        if not node_to_remove:
            return False
        if self.size == 1:
            self.root = None
            self.size -= 1
            return True

        parent = node_to_remove.parent
        key_to_remove_height = node_to_remove.height

        # get balancing successor of node_to_remove
        balance_node = None
        if parent.left == node_to_remove:
            balance_node = self.get_rightmost(parent)
        elif parent.right == node_to_remove:
            balance_node = self.get_leftmost(parent)

        restructure = True

        # CASE 1: node has no child node
        if (not node_to_remove.right) and (not node_to_remove.left):
            self._delete_no_child(node_to_remove, parent)

        # CASE 2: node has only one child; replace it by child node
        elif (
            node_to_remove.left
            and not node_to_remove.right
            or (not node_to_remove.left and node_to_remove.right)
        ):
            self._delete_one_child(node_to_remove, parent)

        # CASE 3: Node has 2 child nodes
        elif node_to_remove.left and node_to_remove.right:
            self._delete_two_children(node_to_remove, key_to_remove_height)
            restructure = False

        # restructure if necessary
        if parent and balance_node and restructure:
            self._cut_link_restructuring(balance_node)
        self.size -= 1
        return True

    def _change_nodes(self, deleting_node: AVLNode, replacing_node: AVLNode) -> None:
        """
        Helper function for remove. node_1 is changing places with node_2.
        :return: None
        """
        if deleting_node.parent is None:  # node_1 is root
            self.root = replacing_node
        elif deleting_node == deleting_node.parent.left:  # node_1 is left child
            deleting_node.parent.left = replacing_node
        else:  # node_1 is right child
            deleting_node.parent.right = replacing_node
        if replacing_node is not None:  # change parent relationship
            replacing_node.parent = deleting_node.parent

    def _delete_two_children(
        self, key_to_remove: AVLNode, key_to_remove_height: int
    ) -> None:
        """
        Helper function for deleting a node with two children.
        :param key_to_remove: node to delete
        :param key_to_remove_height: height of node to delete
        :return: None
        """
        right_child = key_to_remove.right
        next_successor = self.get_smallest_recursively(
            right_child
        )  # get next in-order successor of key_to_remove
        if (
            next_successor.parent != key_to_remove
        ):  # make sure it is not a child of itself
            self._change_nodes(next_successor, next_successor.right)  # swap them
            next_successor.right = key_to_remove.right  # change links
            next_successor.right.parent = next_successor
        self._change_nodes(key_to_remove, next_successor)  # swap them
        next_successor.left = key_to_remove.left  # change links
        next_successor.left.parent = next_successor
        next_successor.height = key_to_remove_height

    @staticmethod
    def _delete_one_child(key_to_remove: AVLNode, parent: AVLNode) -> None:
        """
        Helper function for deleting a node with one child.
        :param key_to_remove: node to delete
        :param parent: parent of node to delete
        :return: None
        """
        # Case 2a: child is on the left to key_to_remove
        if key_to_remove.left and not key_to_remove.right:
            child = key_to_remove.left
            if key_to_remove.key <= parent.key:
                parent.left = child
            elif key_to_remove.key > parent.key:
                parent.right = child

        # Case 2b: child is on the right to key_to_remove
        elif not key_to_remove.left and key_to_remove.right:
            child = key_to_remove.right
            if key_to_remove.key <= parent.key:
                parent.left = child
            elif key_to_remove.key > parent.key:
                parent.right = child

    @staticmethod
    def _delete_no_child(key_to_remove: AVLNode, parent: AVLNode) -> None:
        """
        Helper function for deleting a node with no child.
        :param key_to_remove: node to delete
        :param parent: parent of node to delete
        :return: None
        """
        if key_to_remove.key <= parent.key:
            parent.left = None
        elif key_to_remove.key > parent.key:
            parent.right = None

    def _cut_link_restructuring(self, node: AVLNode) -> None:
        """
        Performs the Cut-Link restructuring algorithm
        :param node: node which is being affected
        :return: None
        """
        parent = node.parent  # equal to z in slides
        y = node
        x = None
        while parent:
            grandparent = parent.parent
            parent.height = self._update_single_height(parent)
            if abs(self._get_balance_factor(parent)) <= 1:
                x = y
                y = parent
                parent = parent.parent

            else:
                is_x_left = bool(x == y.left)
                is_y_left = bool(y == parent.left)

                # INORDER
                # create copies to remove unwanted children for traversal
                parent_tmp = deepcopy(
                    parent
                )  # could also be done via tree traversal/copying, but this is faster
                # (and still part of standard library)

                # get relevant children of parent
                (
                    parent_child,
                    x_left,
                    x_right,
                    x_tmp,
                    y_child,
                    y_tmp,
                ) = self._get_children(is_x_left, is_y_left, parent_tmp)

                # create dictionary that stores node references
                # delete child nodes
                child_dict = self._delete_children(
                    parent_child, x_left, x_right, y_child
                )

                # create inorder array of z/parent, but without unnecessary children (as always ;) )
                inorder_array = list(self.inorder(parent_tmp))
                cut_array = (
                    inorder_array.copy()
                )  # again, faster and part of standard library

                # insert Nones into cut_array, at proper index
                self._insert_nones(
                    cut_array, inorder_array, parent_tmp, x_left, x_right, x_tmp, y_tmp
                )

                # re-insert child nodes into cut_array
                self._reinsert_children(child_dict, cut_array)

                # re-insert parent node of subtree into tree
                current_root = self._reinsert_parent(cut_array, grandparent, parent)

                # re-insert x/y/children into tree
                self._update_children(current_root, cut_array)

                node = self.find_by_key(
                    node.key, _return_node=True
                )  # due to copy; still O(log n)
                parent = node.parent
                y = node
                x = None

    def _update_children(self, current_root: AVLNode, cut_array: list) -> None:
        """
        Updates the children of the current root according to slides, s.t. final tree is balanced
        :param current_root: root node of unbalanced subtree
        :param cut_array: array of nodes in inorder traversal
        :return: None
        """
        current_root.left = cut_array[1]
        current_root.right = cut_array[5]
        # also reassign parent
        current_root.left.parent = current_root
        current_root.right.parent = current_root

        current_root.left.height = 1 + max(
            self.get_height(cut_array[0]),
            self.get_height(cut_array[2]),
        )
        current_root.right.height = 1 + max(
            self.get_height(cut_array[4]),
            self.get_height(cut_array[6]),
        )
        current_root.height = 1 + max(
            self.get_height(current_root.right),
            self.get_height(current_root.left),
        )

        current_root.left.left = cut_array[0]
        current_root.left.right = cut_array[2]
        # update parent
        if cut_array[0]:
            current_root.left.right.parent = current_root.left

        if cut_array[2]:
            current_root.left.left.parent = current_root.left

        current_root.right.left = cut_array[4]
        current_root.right.right = cut_array[6]
        # update parent
        if cut_array[6]:
            current_root.right.right.parent = current_root.right

        if cut_array[4]:
            current_root.right.left.parent = current_root.right

    def _reinsert_parent(
        self, cut_array: list, grandparent: AVLNode, parent: AVLNode
    ) -> AVLNode:
        """
        Reinserts the parent node into the tree
        :param cut_array: array of nodes
        :param grandparent: grandparent node
        :param parent: parent node
        :return: root of new subtree
        """
        if parent == self.root:
            parent = cut_array[3]
            current_root = parent
            self.root = current_root
            current_root.parent = None
        elif grandparent.left == parent:
            parent = cut_array[3]
            grandparent.left = parent
            current_root = parent
            current_root.parent = grandparent
        elif grandparent.right == parent:
            parent = cut_array[3]
            grandparent.right = parent
            current_root = parent
            current_root.parent = grandparent
        else:
            raise Exception("Parent not found")
        return current_root

    @staticmethod
    def _reinsert_children(child_dict: defaultdict, inorder_list: list):
        """
        Reinserts children of deleted node into inorder list
        :param child_dict: dictionary of child nodes
        :param inorder_list: list of inorder nodes, without children
        :return: None
        """
        for value in child_dict.values():
            if value["left"]:
                value_in_list = [
                    x if value["parent"].key == x.key else None for x in inorder_list
                ]  # find value in list
                value_in_list = list(filter(None, value_in_list))[0]
                value_in_list.left = value["left"]
                value_in_list.right = value["right"]
            if value["right"]:
                value_in_list = [
                    x if value["parent"].key == x.key else None for x in inorder_list
                ]  # find value in list
                value_in_list = list(filter(None, value_in_list))[0]
                value_in_list.left = value["left"]
                value_in_list.right = value["right"]

    @staticmethod
    def _insert_nones(
        cut_array: list,
        inorder_list: list,
        parent_tmp: AVLNode,
        x_left: AVLNode,
        x_right: AVLNode,
        x_tmp: AVLNode,
        y_tmp: AVLNode,
    ) -> None:
        """
        Inserts None nodes into inorder list at right index.
        """
        x_list = [x if x_tmp.key == x.key else None for x in inorder_list]
        x_list = list(filter(None, x_list))[0]
        if not x_left:
            cut_array.insert(cut_array.index(x_list), None)
        if not x_right:
            cut_array.insert(cut_array.index(x_list) + 1, None)

        y_list = [x if y_tmp.key == x.key else None for x in inorder_list]
        y_list = list(filter(None, y_list))[0]
        if not y_list.left:
            cut_array.insert(cut_array.index(y_list), None)
        if not y_list.right:
            cut_array.insert(cut_array.index(y_list) + 1, None)

        z_list = [x if parent_tmp.key == x.key else None for x in inorder_list]
        z_list = list(filter(None, z_list))[0]
        if not z_list.left:
            cut_array.insert(0, None)
        if not z_list.right:
            cut_array.insert(6, None)

    @staticmethod
    def _delete_children(
        parent_child: AVLNode,
        x_left: AVLNode,
        x_right: AVLNode,
        y_child: AVLNode,
    ):
        """
        Delete unwanted children of a node.
        :param parent_child: parent of the node to be deleted.
        :param x_left: left child of x
        :param x_right: right child of x
        :param y_child: child of y
        :return:
        """
        child_dict = defaultdict(dict)  # dictionary of children to be deleted
        if x_left:
            child_dict["x_left"]["parent"] = x_left
            child_dict["x_left"]["left"] = x_left.left
            child_dict["x_left"]["right"] = x_left.right
            x_left.left = None
            x_left.right = None
        if x_right:
            child_dict["x_right"]["parent"] = x_right
            child_dict["x_right"]["left"] = x_right.left
            child_dict["x_right"]["right"] = x_right.right
            x_right.left = None
            x_right.right = None
        if parent_child:
            child_dict["parent_child"]["parent"] = parent_child
            child_dict["parent_child"]["left"] = parent_child.left
            child_dict["parent_child"]["right"] = parent_child.right
            parent_child.right = None
            parent_child.left = None
        if y_child:
            child_dict["y_child"]["parent"] = y_child
            child_dict["y_child"]["left"] = y_child.left
            child_dict["y_child"]["right"] = y_child.right
            y_child.left = None
            y_child.right = None
        return child_dict

    @staticmethod
    def _get_children(
        is_x_left: bool, is_y_left: bool, parent_tmp: AVLNode
    ) -> Tuple[AVLNode, AVLNode, AVLNode, AVLNode, AVLNode, AVLNode]:
        """
        Get children of a node.
        :param is_x_left: whether x is left child of parent
        :param is_y_left: whether y is left child of parent
        :param parent_tmp: parent node
        :return: proper AVLNode children
        """
        # get children of x and y
        if is_y_left:
            y_tmp = parent_tmp.left
        else:
            y_tmp = parent_tmp.right
        if is_x_left:
            x_tmp = y_tmp.left
        else:
            x_tmp = y_tmp.right

        parent_child = None  # to avoid errors in a few lines
        y_child = None
        if y_tmp == parent_tmp.right:
            parent_child = parent_tmp.left
        elif y_tmp == parent_tmp.left:
            parent_child = parent_tmp.right
        if y_tmp.right == x_tmp:
            y_child = y_tmp.left
        elif y_tmp.left == x_tmp:
            y_child = y_tmp.right
        x_left = x_tmp.left
        x_right = x_tmp.right
        return parent_child, x_left, x_right, x_tmp, y_child, y_tmp

    def _update_single_height(self, node: AVLNode) -> int:
        """
        Update the height of the node.
        :param node: The node to update the height of.
        :return: None
        """
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    @staticmethod
    def get_leftmost(node) -> AVLNode:
        """
        :param node: node of subtree we are in
        :return: leftmost node
        """
        current = node
        while current.left:
            current = current.left  # go left
        return current

    @staticmethod
    def get_rightmost(node) -> AVLNode:
        """
        :param node: node of subtree we are in
        :return: leftmost node
        """
        current = node
        while current.right:
            current = current.right  # go right
        return current

    @staticmethod
    def get_smallest_recursively(node):
        """
        Helper function to get the smallest key in the tree, starting from a specific node (here: node).
        :param node:
        :return:
        """
        current_node = node
        # Go left as long as left child is not None
        while current_node.left is not None:
            current_node = current_node.left
        return current_node  # and return last node where child is not None

    @staticmethod
    def get_height(node) -> int:
        """
        Gets height of node.
        :param node: node in AVLTree
        :return: height of node
        """
        if node:
            return node.height
        # None has height -1
        return -1

    def _get_balance_factor(self, node) -> int:
        """
        Gets balance factor of node.
        :param node: node in AVLTree
        :return: balance factor of node
        """
        if node:
            return self.get_height(node.left) - self.get_height(node.right)
        # Empty node's height is -1
        return -1

    def is_balanced(self, node: AVLNode) -> bool:
        """
        Checks if node is balanced.
        :param node: AVLNode
        :return: whether node is balanced
        """
        # Base condition
        if node is None:
            return True

        # get left and right subtree height
        left_height = self.get_height(self.root.left)
        right_height = self.get_height(self.root.right)

        if (
            (abs(left_height - right_height) <= 1)  # max. tolerated difference
            and self.is_balanced(node.left) is True  # recurse left
            and self.is_balanced(node.right) is True  # recurse right
        ):
            return True
        return False  # unbalanced

    def inorder(
        self, node: AVLNode = None
    ) -> Union[Iterator, Generator[Any, Any, None]]:
        """Yield nodes in inorder."""
        node = node or self.root

        # left, root, right
        def inorder_recursively(current_node) -> Iterator:
            """
            Recursively yield nodes in inorder.
            :param current_node: AVLNode
            :return: Iterator
            """
            if current_node:
                yield from inorder_recursively(current_node.left)
                yield current_node
                yield from inorder_recursively(current_node.right)

        # This is needed in the case that there are no nodes.
        if not node:
            return iter(())
        return inorder_recursively(node)

    def preorder(
        self, node: AVLNode = None
    ) -> Union[Iterator, Generator[Any, Any, None]]:
        """Yield nodes in preorder."""
        node = node or self.root

        # root, left, right
        def preorder_recursively(current_node) -> Iterator:
            """
            Recursively yield nodes in preorder.
            :param current_node: AVLNode
            :return: Iterator
            """
            if current_node:
                yield current_node
                yield from preorder_recursively(current_node.left)
                yield from preorder_recursively(current_node.right)

        if not node:
            return iter(())
        return preorder_recursively(node)

    def postorder(
        self, node: AVLNode = None
    ) -> Union[Iterator, Generator[Any, Any, None]]:
        """Yield nodes in postorder."""
        node = node or self.root

        # left, right, root
        def postorder_recursively(current_node) -> Iterator:
            """
            Recursively yield nodes in postorder.
            :param current_node: AVLNode
            :return: Iterator
            """
            if current_node:
                yield from postorder_recursively(current_node.left)
                yield from postorder_recursively(current_node.right)
                yield current_node

        if not node:
            return iter(())
        return postorder_recursively(node)

    def print_tree(self, node: Union[AVLNode, None], level: int = 0) -> None:
        """
        Prints the tree.
        :param node: starting node
        :param level: level/depth of node
        :return: None
        """
        if node is not None:
            self.print_tree(node.right, level + 1)
            print(" " * 4 * level + "->", node.key)
            self.print_tree(node.left, level + 1)
