import unittest
import powerwall


# This is not quite a test, it's rather a utility that checks a user's config
# is correct.
# First, create a ~/.autohome/powerwall.json file, see powerwall.py for
# structure.
# Then, run the test.
class TestPowerwall(unittest.TestCase):

  def test_connection_checker(self):
    self.assertTrue(powerwall.is_power_on(powerwall.DEFAULT_CFG_FILE))


if __name__ == '__main__':
  unittest.main()