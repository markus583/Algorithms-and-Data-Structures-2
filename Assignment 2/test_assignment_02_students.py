import unittest
import math

from random import random
from datetime import date
from avl_tree import AVLTree

tree = None
testList = None
testListBackUp = None


# noinspection PyUnresolvedReferences
class TestAssignment02(unittest.TestCase):
    def setUp(self):
        pass

    def reset(self):
        global tree
        tree = AVLTree()

    def insert(self, key, value):
        # handle a none tree object
        global tree
        return tree.insert(key, value)

    def insert(self, key):
        # handle a none tree object
        global tree
        return tree.insert(key, float(key))

    def test_size_provided(self):
        global tree
        self.reset()
        self.insert(5)
        self.assertEqual(
            1,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after inserting a node with key 5 into an AVL tree .. first node "
            + "inserted is 5.",
        )
        self.insert(18)
        self.assertEqual(
            2,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after inserting the nodes with key sequence "
            + "5, 18 into an AVL tree",
        )
        self.insert(2)
        self.assertEqual(
            3,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after inserting the nodes with key sequence "
            + "5, 18, 2 into an AVL tree",
        )
        self.insert(8)
        self.assertEqual(
            4,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after inserting the nodes with key sequence "
            + "5, 18, 2, 8 into an AVL tree",
        )
        self.insert(14)
        self.assertEqual(
            5,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after inserting the nodes with key sequence "
            + "5, 18, 2, 8, 14 into an AVL tree",
        )

    def test_size_with_insert(self):
        global tree
        self.reset()
        self.assertEqual(0, tree.get_tree_size())
        self.insert(5)
        self.assertEqual(
            1,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after inserting a node with key 5 into an AVL tree .. first node "
            + "inserted is 5",
        )
        self.insert(18)
        self.assertEqual(
            2,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after inserting the nodes with keys "
            + "5, 18 into an AVL tree",
        )
        self.insert(2)
        self.assertEqual(
            3,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after inserting the nodes with keys "
            + "5, 18, 2 into an AVL tree",
        )
        self.insert(8)
        self.assertEqual(
            4,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after inserting the nodes with keys "
            + "5, 18, 2, 8 into an AVL tree",
        )
        self.insert(14)
        self.assertEqual(
            5,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after inserting the nodes with keys "
            + "5, 18, 2, 8, 14 into an AVL tree",
        )
        self.insert(16)
        self.assertEqual(
            6,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after inserting the nodes with keys "
            + "5, 18, 2, 8, 14, 16 into an AVL tree",
        )
        self.insert(13)
        self.assertEqual(
            7,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after inserting the nodes with keys "
            + "5, 18, 2, 8, 14, 16, 13 into an AVL tree",
        )
        self.insert(3)
        self.assertEqual(
            8,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after inserting the nodes with keys "
            + "5, 18, 2, 8, 14, 16, 13, 3 into an AVL tree",
        )
        self.insert(12)
        self.assertEqual(
            9,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after inserting the nodes with keys "
            + "5, 18, 2, 8, 14, 16, 13, 3, 12 into an AVL tree",
        )
        self.insert(21)
        self.assertEqual(
            10,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after inserting the nodes with keys "
            + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21 into an AVL tree",
        )
        self.insert(1)
        self.assertEqual(
            11,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after inserting the nodes with keys "
            + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1 into an AVL tree",
        )
        self.insert(0)
        self.assertEqual(
            12,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after inserting the nodes with keys "
            + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0 into an AVL tree",
        )

    def test_height_empty_tree(self):
        global tree
        self.reset()
        self.assertEqual(
            -1, tree.get_tree_height(), ".get_tree_height() is wrong for empty tree:"
        )

    def test_height(self):
        global tree
        self.reset()

        self.assertEqual(
            -1, tree.get_tree_height(), ".get_tree_height() is wrong for empty tree: "
        )
        self.insert(5)
        self.assertEqual(
            0,
            tree.get_tree_height(),
            ".get_tree_height() is wrong after inserting the node with key 5 into an empty AVL tree .. "
            + "first node inserted is 5",
        )
        self.insert(18)
        self.assertEqual(
            1,
            tree.get_tree_height(),
            ".get_tree_height() is wrong after inserting the nodes with keys "
            + "5, 18 into an AVL tree",
        )
        self.insert(2)
        self.assertEqual(
            1,
            tree.get_tree_height(),
            ".get_tree_height() is wrong after inserting the nodes with keys "
            + "5, 18, 2 into an AVL tree",
        )
        self.insert(8)
        self.assertEqual(
            2,
            tree.get_tree_height(),
            ".get_tree_height() is wrong after inserting the nodes with keys "
            + "5, 18, 2, 8 into an AVL tree",
        )
        self.insert(14)
        self.assertEqual(
            2,
            tree.get_tree_height(),
            ".get_tree_height() is wrong after inserting the nodes with keys "
            + "5, 18, 2, 8, 14 into an AVL tree",
        )
        self.insert(16)
        self.assertEqual(
            2,
            tree.get_tree_height(),
            ".get_tree_height() is wrong after inserting the nodes with keys "
            + "5, 18, 2, 8, 14, 16 into an AVL tree",
        )
        self.insert(13)
        self.assertEqual(
            3,
            tree.get_tree_height(),
            ".get_tree_height() is wrong after inserting the nodes with keys "
            + "5, 18, 2, 8, 14, 16, 13 into an AVL tree",
        )
        self.insert(3)
        self.assertEqual(
            3,
            tree.get_tree_height(),
            ".get_tree_height() is wrong after inserting the nodes with keys "
            + "5, 18, 2, 8, 14, 16, 13, 3 into an AVL tree",
        )
        self.insert(12)
        self.assertEqual(
            3,
            tree.get_tree_height(),
            ".get_tree_height() is wrong after inserting the nodes with keys "
            + "5, 18, 2, 8, 14, 16, 13, 3, 12 into an AVL tree",
        )
        self.insert(21)
        self.assertEqual(
            3,
            tree.get_tree_height(),
            ".get_tree_height() is wrong after inserting the nodes with keys "
            + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21 into an AVL tree",
        )
        self.insert(1)
        self.assertEqual(
            3,
            tree.get_tree_height(),
            ".get_tree_height() is wrong after inserting the nodes with keys "
            + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1 into an AVL tree",
        )
        self.insert(0)
        self.assertEqual(
            3,
            tree.get_tree_height(),
            ".get_tree_height() is wrong after inserting the nodes with keys "
            + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0 into an AVL tree",
        )

    def test_find(self):
        global tree
        self.reset()
        self.insert(5)
        self.insert(18)
        self.insert(2)
        self.insert(8)
        self.insert(14)
        self.insert(16)
        self.insert(13)
        self.insert(3)
        self.insert(12)
        self.insert(21)
        self.insert(1)
        self.insert(0)
        self.assertEqual(
            5,
            tree.find_by_key(5),
            ".find_by_key(5) didn't return correct element of the following AVL tree with \n\tthe following "
            + "inserted nodes: "
            + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0",
        )
        self.assertEqual(
            18,
            tree.find_by_key(18),
            ".find_by_key(18) didn't return correct element of the following AVL tree with \n\tthe "
            + "following inserted nodes: "
            + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0",
        )
        self.assertEqual(
            2,
            tree.find_by_key(2),
            ".find_by_key(2) didn't return correct element of the following AVL tree with \n\tthe following "
            + "inserted nodes: "
            + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0",
        )
        self.assertEqual(
            8,
            tree.find_by_key(8),
            ".find_by_key(8) didn't return correct element of the following AVL tree with \n\tthe following "
            + "inserted nodes: "
            + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0",
        )
        self.assertEqual(
            14,
            tree.find_by_key(14),
            ".find_by_key(14) didn't return correct element of the following AVL tree with \n\tthe "
            + "following inserted nodes: "
            + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0",
        )
        self.assertEqual(
            16,
            tree.find_by_key(16),
            ".find_by_key(16) didn't return correct element of the following AVL tree with \n\tthe "
            + "following inserted nodes: "
            + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0",
        )
        self.assertEqual(
            13,
            tree.find_by_key(13),
            ".find_by_key(13) didn't return correct element of the following AVL tree with \n\tthe "
            + "following inserted nodes: "
            + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0",
        )
        self.assertEqual(
            3,
            tree.find_by_key(3),
            ".find_by_key(3) didn't return correct element of the following AVL tree with \n\tthe following "
            + "inserted nodes: "
            + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0",
        )
        self.assertEqual(
            12,
            tree.find_by_key(12),
            ".find_by_key(12) didn't return correct element of the following AVL tree with \n\tthe "
            + "following inserted nodes: "
            + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0",
        )
        self.assertEqual(
            21,
            tree.find_by_key(21),
            ".find_by_key(21) didn't return correct element of the following AVL tree with \n\tthe "
            + "following inserted nodes: "
            + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0",
        )
        self.assertEqual(
            1,
            tree.find_by_key(1),
            ".find_by_key(1) didn't return correct element of the following AVL tree with \n\tthe following "
            + "inserted nodes: "
            + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0",
        )
        self.assertEqual(
            0,
            tree.find_by_key(0),
            ".find_by_key(0) didn't return correct element of the following AVL tree with \n\tthe following "
            + "inserted nodes: "
            + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0",
        )

    def test_find_not_existing(self):
        global tree
        self.reset()
        self.insert(5)
        self.insert(18)
        self.insert(2)
        self.insert(8)
        self.insert(14)
        self.insert(16)
        self.insert(13)
        self.insert(3)
        self.insert(12)
        self.insert(21)
        self.insert(1)
        self.insert(0)
        self.assertEqual(
            None,
            tree.find_by_key(4),
            ".find_by_key() didn't return None when searching for a not existing key.",
        )
        self.assertEqual(
            None,
            tree.find_by_key(99),
            ".find_by_key() didn't return None when searching for a not existing key.",
        )
        self.assertEqual(
            None,
            tree.find_by_key(100),
            ".find_by_key() didn't return None when searching for a not existing key.",
        )

    def test_find_not_existing_empty_tree(self):
        global tree
        self.reset()
        self.assertEqual(
            None,
            tree.find_by_key(4),
            ".find_by_key() didn't return None when searching for a not existing key in an empty tree.",
        )
        self.assertEqual(
            None,
            tree.find_by_key(99),
            ".find_by_key() didn't return None when searching for a not existing key in an empty tree.",
        )
        self.assertEqual(
            None,
            tree.find_by_key(100),
            ".find_by_key() didn't return None when searching for a not existing key in an empty tree.",
        )

    def test_remove(self):
        global tree
        self.reset()
        self.insert(5)
        self.insert(18)
        self.insert(2)
        self.insert(8)
        self.insert(14)
        self.insert(16)
        self.insert(13)
        self.insert(3)
        self.insert(12)
        self.insert(21)
        self.insert(1)
        self.insert(0)
        self.assertFalse(
            tree.remove_by_key(4),
            ".remove_by_key(4) didn't return FALSE for the following AVL tree",
        )
        self.assertFalse(
            tree.remove_by_key(99),
            ".remove_by_key(99) didn't return FALSE for the following AVL tree",
        )
        self.assertFalse(
            tree.remove_by_key(100),
            ".remove_by_key(100) didn't return FALSE for the following AVL tree",
        )

        self.assertTrue(
            tree.remove_by_key(14),
            ".remove_by_key(14) didn't return TRUE for the following AVL tree",
        )
        self.assertTrue(
            tree.remove_by_key(3),
            ".remove_by_key(3) didn't return TRUE for the following AVL tree",
        )
        self.assertTrue(
            tree.remove_by_key(21),
            ".remove_by_key(21) didn't return TRUE for the following AVL tree",
        )
        self.assertTrue(
            tree.remove_by_key(18),
            ".remove_by_key(18) didn't return TRUE for the following AVL tree",
        )
        self.assertTrue(
            tree.remove_by_key(16),
            ".remove_by_key(16) didn't return TRUE for the following AVL tree",
        )
        self.assertFalse(
            tree.remove_by_key(14),
            ".remove_by_key(14) didn't return FALSE for the following AVL tree",
        )

    def test_size_with_remove(self):
        global tree
        self.reset()
        self.insert(5)
        self.insert(18)
        self.insert(2)
        self.insert(8)
        self.insert(14)
        self.insert(16)
        self.insert(13)
        self.insert(3)
        self.insert(12)
        self.insert(21)
        self.insert(1)
        self.insert(0)

        sb = self.display()
        tree.remove_by_key(4)
        self.assertEqual(
            12,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after removing not existing node with key 4 from the following "
            + "tree:"
            + sb,
        )
        tree.remove_by_key(99)
        self.assertEqual(
            12,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after removing not existing node with key 99 from the following "
            + "tree:"
            + sb,
        )
        tree.remove_by_key(100)
        self.assertEqual(
            12,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after removing not existing node with key 100 from the following "
            + "tree:"
            + sb,
        )
        tree.remove_by_key(14)
        self.assertEqual(
            11,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after removing node with key 14 from the following tree:"
            + sb,
        )
        sb = self.display()
        tree.remove_by_key(3)
        self.assertEqual(
            10,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after removing node with key 3 from the following tree:"
            + sb,
        )
        sb = self.display()
        tree.remove_by_key(21)
        self.assertEqual(
            9,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after removing node with key 21 from the following tree:"
            + sb,
        )
        sb = self.display()
        tree.remove_by_key(18)
        self.assertEqual(
            8,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after removing node with key 18 from the following tree:"
            + sb,
        )
        sb = self.display()
        tree.remove_by_key(16)
        self.assertEqual(
            7,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after removing node with key 16 from the following tree:"
            + sb,
        )
        sb = self.display()
        tree.remove_by_key(14)
        self.assertEqual(
            7,
            tree.get_tree_size(),
            ".get_tree_size() is wrong after removing not existing node with key 14 from the following "
            + "tree:"
            + sb,
        )

    def test_height_with_remove(self):
        global tree
        self.reset()
        self.insert(5)
        self.insert(18)
        self.insert(2)
        self.insert(8)
        self.insert(14)
        self.insert(16)
        self.insert(13)
        self.insert(3)
        self.insert(12)
        self.insert(21)
        self.insert(1)
        self.insert(0)

        sb = self.display()
        tree.remove_by_key(4)
        self.assertEqual(
            3,
            tree.get_tree_height(),
            ".get_tree_height() is wrong after removing not existing node with key 4 from the following "
            + "tree:"
            + sb,
        )
        tree.remove_by_key(99)
        self.assertEqual(
            3,
            tree.get_tree_height(),
            ".get_tree_height() is wrong after removing not existing node with key 99 from the following "
            + "tree:"
            + sb,
        )
        tree.remove_by_key(100)
        self.assertEqual(
            3,
            tree.get_tree_height(),
            ".get_tree_height() is wrong after removing not existing node with key 100 from the "
            + "following tree:"
            + sb,
        )
        tree.remove_by_key(14)
        self.assertEqual(
            3,
            tree.get_tree_height(),
            ".get_tree_height() is wrong after removing node with key 14 from the following tree:"
            + sb,
        )
        sb = self.display()
        tree.remove_by_key(3)
        self.assertEqual(
            3,
            tree.get_tree_height(),
            ".get_tree_height() is wrong after removing node with key 3 from the following tree:"
            + sb,
        )
        sb = self.display()
        tree.remove_by_key(21)
        self.assertEqual(
            3,
            tree.get_tree_height(),
            ".get_tree_height() is wrong after removing node with key 21 from the following tree:"
            + sb,
        )
        sb = self.display()
        tree.remove_by_key(18)
        self.assertEqual(
            3,
            tree.get_tree_height(),
            ".get_tree_height() is wrong after removing node with key 18 from the following tree:"
            + sb,
        )
        sb = self.display()
        tree.remove_by_key(16)
        self.assertEqual(
            2,
            tree.get_tree_height(),
            ".get_tree_height() is wrong after removing node with key 16 from the following tree:"
            + sb,
        )
        sb = self.display()
        tree.remove_by_key(14)
        self.assertEqual(
            2,
            tree.get_tree_height(),
            ".get_tree_height() is wrong after removing not existing node with key 14 from the following "
            + "tree:"
            + sb,
        )

    def test_remove_not_existing_key(self):
        global tree
        self.reset()
        self.assertFalse(
            tree.remove_by_key(10212),
            ".remove_by_key() of a not existing key should return FALSE. ",
        )

    def test_remove_none(self):
        global tree
        self.reset()
        expected_ex = None
        try:
            tree.remove_by_key(None)
        except Exception as e:
            expected_ex = e

        self.assertTrue(
            not (isinstance(ValueError, type(expected_ex))),
            ".remove_by_key() of a None key should throw an ValueError.",
        )

    def test_insert_duplicates(self):
        global tree
        self.reset()
        self.assertTrue(
            self.insert(5),
            ".insert_node() didn't return TRUE when a node with a key is inserted for the first time.",
        )
        self.assertFalse(
            self.insert(5),
            ".insert_node() didn't return FALSE when a node with an already existing key is inserted.",
        )

    def test_size_empty_tree(self):
        global tree
        self.reset()
        self.assertEqual(
            0, tree.get_tree_size(), ".get_tree_size() is wrong for empty tree: "
        )

    def test_structure1_rotation_hardcoded(self):
        global tree

        self.reset()
        self.insert(5)
        self.insert(18)
        self.insert(2)
        self.insert(8)
        self.insert(14)
        root = tree.get_tree_root()

        self.assertEqual(root.key, 5)
        self.assertEqual(root.height, 2)
        # left branch
        self.assertEqual(root.left.key, 2)
        self.assertEqual(root.left.height, 0)
        # right branch
        self.assertEqual(root.right.key, 14)
        self.assertEqual(root.right.height, 1)
        self.assertEqual(root.left.left, None)
        self.assertEqual(root.left.right, None)
        self.assertEqual(root.right.left.key, 8)
        self.assertEqual(root.right.left.height, 0)
        self.assertEqual(root.right.left.left, None)
        self.assertEqual(root.right.left.right, None)
        self.assertEqual(root.right.right.key, 18)
        self.assertEqual(root.right.right.height, 0)
        self.assertEqual(root.right.right.left, None)
        self.assertEqual(root.right.right.right, None)

    def test_to_array(self):
        global tree

        self.reset()
        self.insert(5)
        self.insert(18)
        self.insert(2)
        self.insert(8)
        self.insert(14)
        self.insert(16)
        self.insert(13)
        self.insert(3)
        self.insert(12)
        self.insert(21)
        self.insert(1)
        self.insert(0)

        array = tree.to_array()

        array_to_test = ""
        i = 0
        while i < len(array):
            array_to_test += str(array[i]) + " "
            i += 1

        solution = [5, 2, 1, 0, 3, 14, 12, 8, 13, 18, 16, 21]

        i = 0
        while i < len(solution):
            print("Array: " + str(array[i]) + " Solution: " + str(solution[i]))
            self.assertEqual(
                array[i],
                solution[i],
                "toArray() sequence (preorder) is wrong at idx "
                + str(i)
                + ".\n\tYour array: [ "
                + array_to_test
                + "]"
                + self.display(),
            )
            i += 1

        self.assertEqual(
            len(solution), len(array), "toArray() returns array with wrong size: "
        )

    # Function to convert
    def list_to_string(self, s):

        # initialize an empty string
        str1 = ""

        # traverse in the string
        for ele in s:
            str1 = str1 + ele + ", "

        # return string
        return str1

    # ============================================test_multiple_values==================================================

    def test_multiple_values(self):
        global tree

        value_range = 200

        num_of_operations = 50000
        operation_sequence = []
        self.reset()
        print("----------------------------------------------------------")
        print("testMultipleValues: Checking Integrity after insert/remove")
        print("----------------------------------------------------------")
        i = 0
        while i < num_of_operations:
            check = False
            inserted = 0
            removed = 0
            sb_tree_after = self.display()
            sb_tree_before = self.display()
            val = int(random() * value_range)

            if tree.insert(val, float(val)):
                inserted = 1
                operation_sequence.append(" I: {} ".format(val))
            else:
                operation_sequence.append(" (I: {} )".format(val))

            check = self._check_avl_integrity()

            str_error = (
                " of AVL tree broken after multiple insert/remove (number of operations processed: "
                + str(i)
                + " / "
                + str(num_of_operations)
                + ")\n\t"
            )
            str_error += (
                "--> Insert/Remove sequence (I...Insert; R...Remove; an operation in brackets () was "
                + "unsuccessful because of duplicate or not existing node "
                + "; the very last operation caused the error):\n "
            )
            str_error += self.list_to_string(operation_sequence)
            str_error += (
                "\nTree before insert:\n\t"
                + sb_tree_before
                + "\n\n\tTree after insert:"
                + sb_tree_after
                + "\n\t"
            )

            self.assertTrue(check, "Integrity" + str_error)
            self.assertTrue(
                tree.get_tree_height()
                <= (1.44 * (math.log(tree.get_tree_size() + 2) / math.log(2)) - 0.328),
                "Height" + str_error,
            )

            # print(i)
            if tree.remove_by_key(val):
                inserted = 1
                operation_sequence.append(" R: {} ".format(val))
            else:
                operation_sequence.append(" (R: {} )".format(val))

            sb_tree_after = self.display()

            check = self._check_avl_integrity()

            str_error = (
                " of AVL tree broken after multiple insert/remove (number of operations processed: "
                + str(i)
                + "/"
                + str(num_of_operations)
                + ")\n\t"
            )
            str_error += (
                '--> Insert/Remove sequence (I...Insert; R...Remove; an operation in brackets "()" was '
                + "unsuccessful because of duplicate or not existing node; the very last operation caused "
                + "the error):\n\t "
            )
            str_error += self.list_to_string(operation_sequence)
            str_error += (
                "\nTree before insert:\n\t"
                + sb_tree_before
                + "\n\n\tTree after insert:"
                + sb_tree_after
                + "\n\t"
            )

            self.assertTrue(check, "Integrity" + str_error)
            self.assertTrue(
                tree.get_tree_height()
                <= (1.44 * (math.log(tree.get_tree_size() + 2) / math.log(2)) - 0.328),
                "Height" + str_error,
            )

            i += 1

        print(
            " AVL integrity check successful (number of operations processed: "
            + str(i)
            + "/"
            + str(num_of_operations)
            + ")\n\t"
            + '--> Insert/Remove sequence (I...Insert; R...Remove; operation in brackets "()" was unsuccessful '
            + "because of duplicate or not existing node):\n\t "
            + self.list_to_string(operation_sequence)
        )

    # ==============================================================================================

    def test_structure1(self):
        global tree
        self.reset()
        self.insert(5)
        self.insert(18)
        self.insert(2)
        self.insert(8)
        self.insert(14)
        root = tree.get_tree_root()

        str_error = (
            "Rotation error after inserting the nodes with the keys 5, 18, 2, 8, 14."
        )

        # // test structure
        self.assertEqual(root.key, 5, str_error)
        # // left branch
        self.assertEqual(root.left.key, 2, str_error)
        # // right branch
        self.assertEqual(root.right.key, 14, str_error)
        self.assertEqual(root.left.left, None, str_error)
        self.assertEqual(root.left.right, None, str_error)
        self.assertEqual(root.right.left.key, 8, str_error)
        self.assertEqual(root.right.left.left, None, str_error)
        self.assertEqual(root.right.left.right, None, str_error)
        self.assertEqual(root.right.right.key, 18, str_error)
        self.assertEqual(root.right.right.left, None, str_error)
        self.assertEqual(root.right.right.right, None, str_error)

    def test_structure2(self):
        global tree
        self.reset()
        self.insert(5)
        self.insert(18)
        self.insert(2)
        self.insert(8)
        self.insert(14)
        self.insert(16)
        root = tree.get_tree_root()

        str_error = "Rotation error after inserting the nodes with the keys 5, 18, 2, 8, 14, 16."

        # // test structure
        self.assertEqual(root.key, 14, str_error)
        # // left branch
        self.assertEqual(root.left.key, 5, str_error)
        # // right branch
        self.assertEqual(root.left.left.key, 2, str_error)
        self.assertEqual(root.left.left.left, None, str_error)
        self.assertEqual(root.left.left.right, None, str_error)
        self.assertEqual(root.left.right.key, 8, str_error)
        self.assertEqual(root.left.right.left, None, str_error)
        self.assertEqual(root.left.right.right, None, str_error)
        self.assertEqual(root.right.key, 18, str_error)
        self.assertEqual(root.right.left.key, 16, str_error)
        self.assertEqual(root.right.left.left, None, str_error)
        self.assertEqual(root.right.left.right, None, str_error)
        self.assertEqual(root.right.right, None, str_error)

    def test_structure3(self):
        global tree
        self.reset()
        self.insert(5)
        self.insert(18)
        self.insert(2)
        self.insert(8)
        self.insert(14)
        self.insert(16)
        self.insert(13)
        root = tree.get_tree_root()

        str_error = "Rotation error after inserting the nodes with the keys 5, 18, 2, 8, 14, 16, 13."

        # // test structure
        self.assertEqual(root.key, 14, str_error)
        # // left branch
        self.assertEqual(root.left.key, 5, str_error)
        self.assertEqual(root.left.left.key, 2, str_error)
        self.assertEqual(root.left.left.left, None, str_error)
        self.assertEqual(root.left.left.right, None, str_error)
        self.assertEqual(root.left.right.key, 8, str_error)
        self.assertEqual(root.left.right.left, None, str_error)
        self.assertEqual(root.left.right.right.key, 13, str_error)
        self.assertEqual(root.left.right.right.left, None, str_error)
        self.assertEqual(root.left.right.right.right, None, str_error)
        # // right branch
        self.assertEqual(root.right.key, 18, str_error)
        self.assertEqual(root.right.left.key, 16, str_error)
        self.assertEqual(root.right.left.left, None, str_error)
        self.assertEqual(root.right.left.right, None, str_error)
        self.assertEqual(root.right.right, None, str_error)

    def test_structure4(self):
        global tree
        self.reset()
        self.insert(5)
        self.insert(18)
        self.insert(2)
        self.insert(8)
        self.insert(14)
        self.insert(16)
        self.insert(13)
        self.insert(3)
        root = tree.get_tree_root()

        str_error = "Rotation error after inserting the nodes with the keys 5, 18, 2, 8, 14, 16, 13, 3."

        # // test structure
        self.assertEqual(root.key, 14, str_error)
        # // left branch
        self.assertEqual(root.left.key, 5, str_error)
        self.assertEqual(root.left.left.key, 2, str_error)
        self.assertEqual(root.left.left.left, None, str_error)
        self.assertEqual(root.left.left.right.key, 3, str_error)
        self.assertEqual(root.left.left.right.left, None, str_error)
        self.assertEqual(root.left.left.right.right, None, str_error)
        self.assertEqual(root.left.right.key, 8, str_error)
        self.assertEqual(root.left.right.left, None, str_error)
        self.assertEqual(root.left.right.right.key, 13, str_error)
        self.assertEqual(root.left.right.right.left, None, str_error)
        self.assertEqual(root.left.right.right.right, None, str_error)
        # // right branch
        self.assertEqual(root.right.key, 18, str_error)
        self.assertEqual(root.right.left.key, 16, str_error)
        self.assertEqual(root.right.left.left, None, str_error)
        self.assertEqual(root.right.left.right, None, str_error)
        self.assertEqual(root.right.right, None, str_error)

    def test_structure5(self):
        global tree
        self.reset()
        self.insert(5)
        self.insert(18)
        self.insert(2)
        self.insert(8)
        self.insert(14)
        self.insert(16)
        self.insert(13)
        self.insert(3)
        self.insert(12)
        root = tree.get_tree_root()

        str_error = "Rotation error after inserting the nodes with the keys 5, 18, 2, 8, 14, 16, 13, 3, 12."

        # // test structure
        self.assertEqual(root.key, 14, str_error)
        # // left branch
        self.assertEqual(root.left.key, 5, str_error)
        self.assertEqual(root.left.left.key, 2, str_error)
        self.assertEqual(root.left.left.left, None, str_error)
        self.assertEqual(root.left.left.right.key, 3, str_error)
        self.assertEqual(root.left.left.right.left, None, str_error)
        self.assertEqual(root.left.left.right.right, None, str_error)
        self.assertEqual(root.left.right.key, 12, str_error)
        self.assertEqual(root.left.right.left.key, 8, str_error)
        self.assertEqual(root.left.right.left.left, None, str_error)
        self.assertEqual(root.left.right.left.right, None, str_error)
        self.assertEqual(root.left.right.right.key, 13, str_error)
        self.assertEqual(root.left.right.right.left, None, str_error)
        self.assertEqual(root.left.right.right.right, None, str_error)
        # // right branch
        self.assertEqual(root.right.key, 18, str_error)
        self.assertEqual(root.right.left.key, 16, str_error)
        self.assertEqual(root.right.left.left, None, str_error)
        self.assertEqual(root.right.left.right, None, str_error)
        self.assertEqual(root.right.right, None, str_error)

    def test_structure6(self):
        global tree
        self.reset()
        self.insert(5)
        self.insert(18)
        self.insert(2)
        self.insert(8)
        self.insert(14)
        self.insert(16)
        self.insert(13)
        self.insert(3)
        self.insert(12)
        self.insert(21)
        root = tree.get_tree_root()

        str_error = "Rotation error after inserting the nodes with the keys 5, 18, 2, 8, 14, 16, 13, 3, 12, 21."

        # // test structure
        self.assertEqual(root.key, 14, str_error)
        # // left branch
        self.assertEqual(root.left.key, 5, str_error)
        self.assertEqual(root.left.left.key, 2, str_error)
        self.assertEqual(root.left.left.left, None, str_error)
        self.assertEqual(root.left.left.right.key, 3, str_error)
        self.assertEqual(root.left.left.right.left, None, str_error)
        self.assertEqual(root.left.left.right.right, None, str_error)
        self.assertEqual(root.left.right.key, 12, str_error)
        self.assertEqual(root.left.right.left.key, 8, str_error)
        self.assertEqual(root.left.right.left.left, None, str_error)
        self.assertEqual(root.left.right.left.right, None, str_error)
        self.assertEqual(root.left.right.right.key, 13, str_error)
        self.assertEqual(root.left.right.right.left, None, str_error)
        self.assertEqual(root.left.right.right.right, None, str_error)
        # // right branch
        self.assertEqual(root.right.key, 18, str_error)
        self.assertEqual(root.right.left.key, 16, str_error)
        self.assertEqual(root.right.left.left, None, str_error)
        self.assertEqual(root.right.left.right, None, str_error)
        self.assertEqual(root.right.right.key, 21, str_error)
        self.assertEqual(root.right.right.left, None, str_error)
        self.assertEqual(root.right.right.right, None, str_error)

    def test_structure7(self):
        global tree
        self.reset()
        self.insert(5)
        self.insert(18)
        self.insert(2)
        self.insert(8)
        self.insert(14)
        self.insert(16)
        self.insert(13)
        self.insert(3)
        self.insert(12)
        self.insert(21)
        self.insert(1)
        self.insert(0)
        root = tree.get_tree_root()

        str_error = "Rotation error after inserting the nodes with the keys 5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0."

        # // test structure
        self.assertEqual(root.key, 5, str_error)
        # // left branch
        self.assertEqual(root.left.key, 2, str_error)
        self.assertEqual(root.left.left.key, 1, str_error)
        self.assertEqual(root.left.left.left.key, 0, str_error)
        self.assertEqual(root.left.left.left.left, None, str_error)
        self.assertEqual(root.left.left.left.right, None, str_error)
        self.assertEqual(root.left.left.right, None, str_error)
        self.assertEqual(root.left.right.key, 3, str_error)
        self.assertEqual(root.left.right.left, None, str_error)
        self.assertEqual(root.left.right.right, None, str_error)
        # // right branch
        self.assertEqual(root.right.key, 14, str_error)
        self.assertEqual(root.right.left.key, 12, str_error)
        self.assertEqual(root.right.left.left.key, 8, str_error)
        self.assertEqual(root.right.left.left.left, None, str_error)
        self.assertEqual(root.right.left.left.right, None, str_error)

        self.assertEqual(root.right.left.right.key, 13, str_error)
        self.assertEqual(root.right.left.right.left, None, str_error)
        self.assertEqual(root.right.left.right.right, None, str_error)

        self.assertEqual(root.right.right.key, 18, str_error)
        self.assertEqual(root.right.right.left.key, 16, str_error)
        self.assertEqual(root.right.right.left.left, None, str_error)
        self.assertEqual(root.right.right.left.right, None, str_error)
        self.assertEqual(root.right.right.right.key, 21, str_error)
        self.assertEqual(root.right.right.right.left, None, str_error)
        self.assertEqual(root.right.right.right.right, None, str_error)

    def _check_avl_integrity(self):
        global tree
        return self.check_avl_integrity(tree.get_tree_root())

    def check_avl_integrity(self, n):
        global tree

        is_avl = True
        if n is None:
            return True
        if not self.is_avltree(n):
            is_avl = False

        if not is_avl:
            lh = -1 if n.left is None else n.left.height
            rh = -1 if n.right is None else n.right.height
            print(str(n.height) + ";" + str(lh) + ";" + str(rh))

        if not self.check_avl_integrity(n.left):
            is_avl = False
        if not self.check_avl_integrity(n.right):
            is_avl = False

        return is_avl

    def is_avltree(self, n):
        diff = -1 if n.left is None else n.left.height
        -(-1 if n.right is None else n.right.height)
        return (-1 <= diff) and (diff <= 1)

    def display(self):
        global tree
        height, width = 5, 64
        len = width * height * 2 + 2
        sb = str(len)
        i = 1
        while i <= len:
            sb += "\n" if i < len - 2 and i % width == 0 else " "
            i += 1
        self.display_r(sb, width / 2, 1, width / 4, width, tree.get_tree_root(), " ")
        return sb

    def display_r(self, sb, c, r, d, w, n, edge):
        if n is not None:
            if n != n.left:
                self.display_r(sb, c - d, r + 2, d / 2, w, n.left, " /")

            s = str(n.key)
            idx1 = r * w + c - (len(s) + 1) / 2
            idx2 = idx1 = len(s)
            idx3 = idx1 - w
            if idx2 < len(sb):
                tmp = sb[:idx1] + s + sb[idx2:]
                sb = tmp[:idx3] + edge + tmp[idx3 + 2 :]
            if n != n.right:
                self.display_r(sb, c + d, r + 2, d / 2, w, n.right, "\\ ")


if __name__ == "__main__":
    unittest.main()
