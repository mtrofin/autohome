import datetime
import unittest
import minisplit


class TestMinisplit(unittest.TestCase):

  def test_on(self):
    ms = minisplit.Minisplit()
    self.assertTrue(ms.turn_on())

  def test_off(self):
    ms = minisplit.Minisplit()
    self.assertTrue(ms.turn_off())
  
  def test_modes(self):
    ms = minisplit.Minisplit()
    hr = datetime.datetime.now().hour
    sched = [hr - 1, hr, hr + 1]
    ms._mixed_mode_heating_period = sched
    ms._mode = minisplit.Mode.Cool
    self.assertEqual(ms._get_on_cmd(), ms._cooling_cmd)
    ms._mode = minisplit.Mode.Heat
    self.assertEqual(ms._get_on_cmd(), ms._heating_cmd)
    ms._mode = minisplit.Mode.Mixed
    self.assertEqual(ms._get_on_cmd(), ms._heating_cmd)
    ms._mixed_mode_heating_period = [hr + 2, hr + 3 ]
    self.assertEqual(ms._get_on_cmd(), ms._cooling_cmd)


if __name__ == '__main__':
  unittest.main()