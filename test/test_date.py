import unittest
from todo.date import *
from todo.entry import *

class TestEntry(unittest.TestCase):
    def test_json_out(self):
        # Test 1
        date = Date(2019, 3, 8, 10, 0) # 3/8/19 at 10:00 AM
        entry = Entry("Math Homework", date, 2)
        test_actual = entry.json_out()
        test_expected = "{'description': 'Math Homework', \
                'deadline': {'year': 2019, 'month': 3, 'day': 8, 'hour': 10, 'minute': 0}, \
                'priority': 2}"
        self.assertEqual(test_actual, test_expected)
