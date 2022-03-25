import unittest

def myList():
    list = [1,2,3,"ram",20]
    return list


class MyListChecker(unittest.TestCase):
    def test_list(self):
        element = 1
        self.assertIn(element,myList())


    def test_case1(self):
        element = 23
        self.assertNotIn(element,myList())


if __name__ == "__main__":
    unittest.main()
