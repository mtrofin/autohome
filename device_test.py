import device
import unittest


class TestDevice(device.Device):

  def __init__(self):
    super(TestDevice, self).__init__('test_device', enable_logging=False)
    self._last_status = None
    self._status = None
    self._should_be_on = True

  def _set_status(self, v: bool):
    self._last_status = v

  def _get_last_status(self):
    return self._last_status
  
  def should_be_on(self) -> bool:
    return self._should_be_on
  
  def turn_off(self) -> bool:
    self._status = False
    return True

  def turn_on(self) -> bool:
    self._status = True;
    return True

class TestDeviceLogic(unittest.TestCase):

  def test_on_power_on(self):
    td = TestDevice()
    td.power_is_on()
    self.assertTrue(td._last_status)
    self.assertTrue(td._status)
    td._should_be_on = False
    td.power_is_on()
    self.assertFalse(td._last_status)
    self.assertFalse(td._status)
    td.power_is_on()
    self.assertFalse(td._last_status)
    self.assertFalse(td._status)
    td._should_be_on = True
    td.power_is_on()
    self.assertTrue(td._last_status)
    self.assertTrue(td._status)

  def test_on_power_off(self):
    td = TestDevice()
    self.assertTrue(td._should_be_on)
    td.power_is_off()
    self.assertFalse(td._last_status)
    self.assertFalse(td._status)

  def test_on_off_transition(self):
    td = TestDevice()
    td._last_status=True
    td._status=True
    td.power_is_off()
    self.assertFalse(td._last_status)
    self.assertFalse(td._status)
    td.power_is_off()
    self.assertFalse(td._last_status)
    self.assertFalse(td._status)

  def test_off_on_transition(self):
    td = TestDevice()
    td._last_status=False
    td._status=False
    td.power_is_on()
    self.assertTrue(td._last_status)
    self.assertTrue(td._status)


if __name__ == '__main__':
  unittest.main()