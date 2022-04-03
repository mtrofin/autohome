import unittest
import water_heater


# This is not quite a test, it's rather a utility that checks a user's config
# is correct.
# First, create a ~/.autohome/assistant.json file, see assistant.py for
# structure.
# Then, run the test.
class TestWaterheater(unittest.TestCase):

  def test_get_status(self):
    wh = water_heater.Waterheater()
    self.assertTrue(isinstance(wh.is_it_on(), bool))

  def test_turn_on(self):
    wh = water_heater.Waterheater()
    self.assertTrue(wh.turn_on())

  def test_turn_off(self):
    wh = water_heater.Waterheater()
    self.assertTrue(wh.turn_off())  

if __name__ == '__main__':
  unittest.main()
  