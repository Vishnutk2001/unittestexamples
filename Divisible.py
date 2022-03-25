import sys
import unittest

def check_divisibleby7(x):
    if(x%7==0):
        return True
    else:
        return False

class CheckDivisible(unittest.TestCase):
    @unittest.skipIf(sys.platform.startswith("win"), "requires windows os")
    def test_check_divisible1(self):
        result = check_divisibleby7(14)
        self.assertTrue(result)


    @unittest.skipUnless(sys.platform.startswith("Linux"),"requires not windows os")
    def test_check_divisible2(self):
        result = check_divisibleby7(13)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()