import unittest
import minisplit


class TestMinisplit(unittest.TestCase):

  def test_on(self):
    ms = minisplit.Minisplit()
    self.assertTrue(ms.turn_on())

  def test_off(self):
    ms = minisplit.Minisplit()
    self.assertTrue(ms.turn_off())

if __name__ == '__main__':
  unittest.main()