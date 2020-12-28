import unittest


class TestDemo1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("#" * 30)
        print("Przed testem")
        print("#" * 30)

    def setUp(self):
        print("Wykonanae przed każdym testem")

    def test_A(self):
        print("test A")

    def test_B(self):
        print("test B")

    def test_C(self):
        a = True
        self.assertTrue(a, "A is not Truee")

    def test_D(self):
        a = "alfa"
        b = "alfa"
        self.assertEqual(a, b, "a is not egual b ")

    def test_E(self):
        a = 5
        b = 3
        self.assertLess(a, b, "B is less than A ")

    def test_F(self):
        a = 2
        b = 2
        self.assertIs(a, b)

    def test_G(self):
        a = 6
        b = 5
        self.assertGreater(a, b, "a is not greater than b")

    def tearDown(self):
        print("Wykonane po każdym tescie")

    @classmethod
    def tearDownClass(cls):
        print("#" * 30)
        print("Po teście")
        print("#" * 30)


if __name__ == '__main__':
    unittest.main()