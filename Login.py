import unittest

def Login(username,password):
    if username == "admin" and password == "12345":
        return True
    else:
        return False


class Logincheck(unittest.TestCase):

    def test_login_check(self):
        username = "admin"
        password = "12345"
        result = Login(username,password)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()