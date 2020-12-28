import unittest
from demo import TestDemo
from demo1 import TestDemo1

tc1= unittest.TestLoader().loadTestsFromTestCase(TestDemo)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestDemo1)

suit = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner().run(suit)