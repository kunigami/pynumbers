import unittest
from mod_division import mod_division
from mod_exp import mod_exp

class TestStringMethods(unittest.TestCase):
  def test_dividing_by_itself(self):
    self.assertEqual(mod_division(12, 12, 13), 1)

  def test_dividing_by_one(self):
    self.assertEqual(mod_division(12, 1, 13), 12)

  def test_random_values(self):
    self.assertEqual(mod_division(1, 11, 13), 6)

  def test_dividing_by_zero(self):
    with self.assertRaises(ZeroDivisionError) as raised:
      mod_division(12, 13, 13)
    exp = raised.exception
    self.assertEqual(exp.message.strip(), "division by 0")


if __name__ == '__main__':
    unittest.main()
