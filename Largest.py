import unittest

def Largest_numbers(x,y):
    if (x>y):
        return True
    else:
        return False

class Check_largest(unittest.TestCase):
    def test_case_largest1(self):
        a = 10
        b = 20
        c = (a,b)
        self.assertTrue(c,b)

    def test_case_largest2(self):
        a = 20
        b = 10
        c = (a,b)
        self.assertTrue(c,a)





if __name__ == "__main__":
    unittest.main()