import unittest
import assistant


# This is not quite a test, it's rather a utility that checks a user's config
# is correct.
# First, create a ~/.autohome/assistant.json file, see assistant.py for
# structure.
# Then, run the test.
class TestPowerwall(unittest.TestCase):

  def test_turn_on(self):
    self.assertTrue(assistant.turn_on(assistant.DEFAULT_CFG_FILE))

  def test_turn_off(self):
    self.assertTrue(assistant.turn_off(assistant.DEFAULT_CFG_FILE))

if __name__ == '__main__':
  unittest.main()
  