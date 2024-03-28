from unittest import TestCase

from dllist import DLList


class TestDLList(TestCase):
    def test_to_array(self):
        t1 = [1, 2, 5, 1, 2, 6, 1, 6, 8, 324, -10, 20]
        t2 = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 2, 3]
        self.assertEqual(t1, DLList.from_array(t1).to_array())
        self.assertEqual(t2, DLList.from_array(t2).to_array())
        self.assertNotEqual(t2, DLList.from_array(t1).to_array())

    def test_size(self):
        cases = [
            # list, expected size
            ([1, 2, 3, 4, 5, 6], 6),
            ([1], 1),
            ([], 0)
        ]
        for source, size in cases:
            with self.subTest(source=source):
                self.assertEqual(DLList.from_array(source).get_size(), size)

    def test_push_and_pop(self):
        l = DLList()
        l.push_front(1)
        l.push_front(2)
        l.push_front(3)
        l.push_back(4)
        l.push_back(5)
        l.push_back(6)
        self.assertEqual(l.to_array(), [3, 2, 1, 4, 5, 6])

        self.assertEqual(l.pop_back(), 6)
        self.assertEqual(l.pop_back(), 5)
        self.assertEqual(l.pop_front(), 3)

        self.assertEqual(l.to_array(), [2, 1, 4])

    def test_remove_and_insert_after(self):
        l = DLList()
        for _ in range(10):
            l.push_back(1)

        for i in range(9, -1, -1):
            l.insert_after(l.get_at(i), i)

        self.assertEqual(l.to_array(), [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9])

        for i in range(9, -1, -1):
            l.remove(l.get_at(2 * i))

        self.assertEqual(l.to_array(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(l.get_size(), 10)

        for _ in range(10):
            l.pop_back()
        self.assertEqual(l.get_size(), 0)

        for _ in range(7):
            l.push_front(1)
            l.push_back(2)
        self.assertEqual(l.get_size(), 14)

        for _ in range(14):
            l.pop_front()
        self.assertEqual(l.get_size(), 0)

        l.push_front(1)
        self.assertEqual(l.end.x, 1)

        l.pop_back()
        l.push_back(2)
        self.assertEqual(l.begin.x, 2)

        l.pop_front()
        l.push_back(7)
        self.assertEqual(l.end.x, 7)
