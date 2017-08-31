import unittest
from skewedBinaryNumber import decimalToSkewedBinary

class TestStringMethods(unittest.TestCase):

    def testConvertingFromDecimalToSkewedBinary(self):
        for data in self.getTestData():
            inputDecimal, expected = data
            self.assertEqual(decimalToSkewedBinary(inputDecimal), expected)

    def getTestData(self):
        return [
            (0, [0]),
            (1, [1]),
            (2, [2]),
            (3, [1, 0]),
            (4, [1, 1]),
            (5, [1, 2]),
            (6, [2, 0]),
            (7, [1, 0, 0]),
            (8, [1, 0, 1]),
            (9, [1, 0, 2]),
            (10, [1, 1, 0]),
        ]

if __name__ == '__main__':
    unittest.main()
