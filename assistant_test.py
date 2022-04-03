import unittest
import assistant


# This is not quite a test, it's rather a utility that checks a user's config
# is correct.
# First, create a ~/.autohome/assistant.json file, see assistant.py for
# structure.
# Then, run the test.
class TestAssistant(unittest.TestCase):

  def test_turn_on(self):
    a = assistant.Assistant()
    self.assertTrue(a.turn_on())

  def test_turn_off(self):
    a = assistant.Assistant()
    self.assertTrue(a.turn_off())

if __name__ == '__main__':
  unittest.main()
  