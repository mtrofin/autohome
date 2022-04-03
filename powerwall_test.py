import unittest
import powerwall


class TestPowerwall(unittest.TestCase):

  def test_connection_checker(self):
    pw = powerwall.Powerwall()
    self.assertTrue(pw.is_power_on())


if __name__ == '__main__':
  unittest.main()