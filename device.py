from abc import abstractmethod
import syslog
import status

DEBUG = syslog.LOG_DEBUG
ERROR = syslog.LOG_ERR

def _no_log(level, msg, *args, **kwargs):
  pass

class Device:

  def __init__(self, name, enable_logging=True):
    self._name = name
    self._logger = syslog.syslog if enable_logging else _no_log

  def log(self, level, msg, *args, **kwargs):
    self._logger(level, '[{0}]: {1}'.format(self._name, msg), *args, **kwargs)  

  def _get_last_status(self):
    retval = status.get_status(self._name)
    self._logger(DEBUG, 'last status is: {0}'.format(retval))
    return retval

  def _set_status(self, v:bool):
    self._logger(DEBUG, 'setting status: {0}'.format(v))
    status.set_status(self._name, v)

  def _turn_off_impl(self):
    self.log(DEBUG, 'telling device to switch off')
    if self.turn_off():
      self.log(DEBUG, 'turned device off')
      self._set_status(False)
      return True
    self.log(ERROR, 'could not turn device off')
    return False

  def power_is_on(self):
    self.log(DEBUG, 'power is on')
    last_status = self._get_last_status()
    should_be_on = self.should_be_on()
    self.log(DEBUG, 'schedule says: {0}'.format(should_be_on))
    if last_status == should_be_on:
      self.log(DEBUG, 'device is already set correctly, doing nothing')
      return True
    if not should_be_on and last_status:
      return self._turn_off_impl()
    assert should_be_on
    if self.turn_on():
      self.log(DEBUG, 'turned device on')
      self._set_status(True)
      return True
    self.log(ERROR, 'could not turn device on')
    return False

  def power_is_off(self):
    self.log(DEBUG, 'power is off')
    s = self._get_last_status()
    if s is not None and not s:
      self.log(DEBUG, 'last status was off, doing nothing')
      return True
    return self._turn_off_impl()

  @abstractmethod
  def turn_off(self)->bool:
    ...

  @abstractmethod
  def turn_off(self)->bool:
    ...

  def should_be_on(self)->bool:
    return True