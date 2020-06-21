from rerange import rearrange_name
import unittest

class TestRearange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)
    def test_one_name(self):
        testcase = "Hopper"
        expected = "Hopper"
        self.assertEqual(rearrange_name(testcase), expected)
        
if __name__ == '__main__':
    unittest.main()
