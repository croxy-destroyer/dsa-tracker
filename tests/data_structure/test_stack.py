import unittest
from src.data_structure.stack.stack import Stack


class TestNormalCases(unittest.TestCase):
    """Normal Cases (Happy Path) — standard expected behavior"""

    def setUp(self):
        """Runs before each test: stack with [1,2,3,4], top=4"""
        self.stack = Stack()
        for i in [1, 2, 3, 4]:
            self.stack.push(i)

    # ── push ──────────────────────────────────────
    def test_push_updates_top(self):
        self.stack.push(99)
        self.assertEqual(self.stack.peek(), 99)

    def test_push_increases_size(self):
        before = self.stack.size()
        self.stack.push(99)
        self.assertEqual(self.stack.size(), 5)

    def test_push_order_is_lifo(self):
        self.assertEqual(self.stack.to_list(), [4, 3, 2, 1])

    # ── pop ───────────────────────────────────────
    def test_pop_returns_top(self):
        self.assertEqual(self.stack.pop(), 4)

    def test_pop_removes_top(self):
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 3)

    def test_pop_decreases_size(self):
        self.stack.pop()
        self.assertEqual(self.stack.size(), 3)

    def test_pop_all_elements_in_order(self):
        result = [self.stack.pop() for _ in range(4)]
        self.assertEqual(result, [4, 3, 2, 1])

    # ── peek ──────────────────────────────────────
    def test_peek_returns_top(self):
        self.assertEqual(self.stack.peek(), 4)

    def test_peek_does_not_remove_element(self):
        self.stack.peek()
        self.assertEqual(self.stack.size(), 4)

    # ── is_empty ──────────────────────────────────
    def test_is_empty_false_when_has_elements(self):
        self.assertFalse(self.stack.is_empty())

    def test_is_empty_true_after_all_popped(self):
        for _ in range(4):
            self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    # ── size / len ────────────────────────────────
    def test_size_returns_correct_count(self):
        self.assertEqual(self.stack.size(), 4)

    def test_len_returns_correct_count(self):
        self.assertEqual(len(self.stack), 4)

    def test_size_and_len_are_equal(self):
        self.assertEqual(self.stack.size(), len(self.stack))

    # ── clear ─────────────────────────────────────
    def test_clear_empties_stack(self):
        self.stack.clear()
        self.assertTrue(self.stack.is_empty())

    def test_clear_resets_size_to_zero(self):
        self.stack.clear()
        self.assertEqual(self.stack.size(), 0)

    # ── to_list ───────────────────────────────────
    def test_to_list_returns_top_to_bottom(self):
        self.assertEqual(self.stack.to_list(), [4, 3, 2, 1])

    def test_to_list_does_not_modify_stack(self):
        self.stack.to_list()
        self.assertEqual(self.stack.size(), 4)

    # ── search ────────────────────────────────────
    def test_search_top_element_depth_one(self):
        self.assertEqual(self.stack.search(4), 1)

    def test_search_bottom_element(self):
        self.assertEqual(self.stack.search(1), 4)

    def test_search_middle_element(self):
        self.assertEqual(self.stack.search(3), 2)

    # ── min / max ─────────────────────────────────
    def test_min_returns_smallest(self):
        self.assertEqual(self.stack.min(), 1)

    def test_max_returns_largest(self):
        self.assertEqual(self.stack.max(), 4)

    # ── __str__ ───────────────────────────────────
    def test_str_format(self):
        self.assertEqual(str(self.stack), "TOP → [4, 3, 2, 1] → BOTTOM")


class TestEdgeCases(unittest.TestCase):
    """Edge Cases — extreme but valid inputs"""

    def setUp(self):
        self.stack = Stack()

    # ── single element ────────────────────────────
    def test_push_and_pop_single_element(self):
        self.stack.push(42)
        self.assertEqual(self.stack.pop(), 42)
        self.assertTrue(self.stack.is_empty())

    def test_peek_single_element(self):
        self.stack.push(42)
        self.assertEqual(self.stack.peek(), 42)

    def test_size_single_element(self):
        self.stack.push(42)
        self.assertEqual(self.stack.size(), 1)

    def test_clear_single_element(self):
        self.stack.push(42)
        self.stack.clear()
        self.assertTrue(self.stack.is_empty())

    def test_min_single_element(self):
        self.stack.push(42)
        self.assertEqual(self.stack.min(), 42)

    def test_max_single_element(self):
        self.stack.push(42)
        self.assertEqual(self.stack.max(), 42)

    def test_search_single_element(self):
        self.stack.push(42)
        self.assertEqual(self.stack.search(42), 1)

    def test_to_list_single_element(self):
        self.stack.push(42)
        self.assertEqual(self.stack.to_list(), [42])

    def test_str_single_element(self):
        self.stack.push(42)
        self.assertEqual(str(self.stack), "TOP → [42] → BOTTOM")

    # ── special values ────────────────────────────
    def test_push_none(self):
        self.stack.push(None)
        self.assertIsNone(self.stack.peek())

    def test_push_zero(self):
        self.stack.push(0)
        self.assertEqual(self.stack.peek(), 0)

    def test_push_negative(self):
        self.stack.push(-99)
        self.assertEqual(self.stack.peek(), -99)

    def test_push_float(self):
        self.stack.push(3.14)
        self.assertEqual(self.stack.peek(), 3.14)

    def test_push_string(self):
        self.stack.push("hello")
        self.assertEqual(self.stack.peek(), "hello")

    def test_push_list_as_value(self):
        self.stack.push([1, 2, 3])
        self.assertEqual(self.stack.peek(), [1, 2, 3])

    def test_push_duplicate_values(self):
        for _ in range(3):
            self.stack.push(5)
        self.assertEqual(self.stack.to_list(), [5, 5, 5])

    # ── search duplicates ─────────────────────────
    def test_search_returns_shallowest_duplicate(self):
        """When duplicates exist, search should return first match from top"""
        for v in [1, 5, 5, 5]:
            self.stack.push(v)
        self.assertEqual(self.stack.search(5), 1)  # topmost 5 is at depth 1

    # ── min / max with negatives ──────────────────
    def test_min_all_negatives(self):
        for v in [-1, -5, -3]:
            self.stack.push(v)
        self.assertEqual(self.stack.min(), -5)

    def test_max_all_negatives(self):
        for v in [-1, -5, -3]:
            self.stack.push(v)
        self.assertEqual(self.stack.max(), -1)

    def test_min_with_zero(self):
        for v in [1, 0, 2]:
            self.stack.push(v)
        self.assertEqual(self.stack.min(), 0)

    def test_max_with_zero(self):
        for v in [-1, 0, -2]:
            self.stack.push(v)
        self.assertEqual(self.stack.max(), 0)

    def test_min_all_same(self):
        for _ in range(4):
            self.stack.push(7)
        self.assertEqual(self.stack.min(), 7)

    def test_max_all_same(self):
        for _ in range(4):
            self.stack.push(7)
        self.assertEqual(self.stack.max(), 7)

    # ── push then pop then push again ─────────────
    def test_push_pop_push_size_correct(self):
        self.stack.push(1)
        self.stack.pop()
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 1)
        self.assertEqual(self.stack.peek(), 2)

    # ── is_empty after clear ──────────────────────
    def test_is_empty_after_clear(self):
        self.stack.push(1)
        self.stack.clear()
        self.assertTrue(self.stack.is_empty())

    # ── to_list empty stack ───────────────────────
    def test_to_list_empty(self):
        self.assertEqual(self.stack.to_list(), [])

    # ── str when empty ────────────────────────────
    def test_str_empty_stack(self):
        self.assertEqual(str(self.stack), "Stack: empty")

    # ── large number of pushes ────────────────────
    def test_large_push_size(self):
        for i in range(1000):
            self.stack.push(i)
        self.assertEqual(self.stack.size(), 1000)
        self.assertEqual(self.stack.peek(), 999)

    def test_large_push_min_max(self):
        for i in range(1, 1001):
            self.stack.push(i)
        self.assertEqual(self.stack.min(), 1)
        self.assertEqual(self.stack.max(), 1000)


class TestFailCases(unittest.TestCase):
    """Fail Cases — invalid inputs that must raise exceptions"""

    def setUp(self):
        self.stack = Stack()

    # ── pop on empty ──────────────────────────────
    def test_pop_empty_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_pop_empty_error_message(self):
        with self.assertRaises(IndexError) as ctx:
            self.stack.pop()
        self.assertIn("Stack Underflow", str(ctx.exception))

    # ── peek on empty ─────────────────────────────
    def test_peek_empty_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.stack.peek()

    def test_peek_empty_error_message(self):
        with self.assertRaises(IndexError) as ctx:
            self.stack.peek()
        self.assertIn("Stack is empty", str(ctx.exception))

    # ── clear on empty ────────────────────────────
    def test_clear_empty_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.stack.clear()

    def test_clear_empty_error_message(self):
        with self.assertRaises(IndexError) as ctx:
            self.stack.clear()
        self.assertIn("already empty", str(ctx.exception))

    # ── search on empty ───────────────────────────
    def test_search_empty_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.stack.search(1)

    # ── search value not found ────────────────────
    def test_search_not_found_raises_value_error(self):
        for i in [1, 2, 3]:
            self.stack.push(i)
        with self.assertRaises(ValueError):
            self.stack.search(99)

    def test_search_not_found_error_message(self):
        self.stack.push(1)
        with self.assertRaises(ValueError) as ctx:
            self.stack.search(99)
        self.assertIn("99", str(ctx.exception))
        self.assertIn("not found", str(ctx.exception))

    # ── min on empty ──────────────────────────────
    def test_min_empty_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.stack.min()

    # ── max on empty ──────────────────────────────
    def test_max_empty_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.stack.max()

    # ── pop more than pushed ──────────────────────
    def test_pop_more_than_pushed(self):
        self.stack.push(1)
        self.stack.pop()
        with self.assertRaises(IndexError):
            self.stack.pop()  # stack is now empty

    # ── size stays consistent after failed ops ────
    def test_size_unchanged_after_failed_pop(self):
        self.stack.push(1)
        try:
            self.stack.pop()
            self.stack.pop()  # this will fail
        except IndexError:
            pass
        self.assertEqual(self.stack.size(), 0)

    def test_size_unchanged_after_failed_peek(self):
        try:
            self.stack.peek()
        except IndexError:
            pass
        self.assertEqual(self.stack.size(), 0)

    # ── double clear ──────────────────────────────
    def test_clear_twice_raises_on_second(self):
        self.stack.push(1)
        self.stack.clear()
        with self.assertRaises(IndexError):
            self.stack.clear()

