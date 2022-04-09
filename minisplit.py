""" Control a minisplit via IR. """

import broadlink
import device
import datetime
import enum
import gin
import os

from pathlib import Path
from typing import List

@gin.constants_from_enum
class Mode(enum.Enum):
  Invalid = 0
  Heat = 1
  Cool = 2
  Mixed = 3

@gin.configurable
class Minisplit(device.Device):

  def __init__(self, heating_cmd: bytes, cooling_cmd: bytes, mode: Mode,
               off_cmd: bytes, schedule: List[int],
               mixed_mode_heating_period: List[int]):
    super(Minisplit, self).__init__('minisplit')
    assert mode != Mode.Invalid
    self._mode = mode
    self._heating_cmd = heating_cmd
    self._cooling_cmd = cooling_cmd
    self._off_cmd = off_cmd
    self._device = broadlink.discover()[0]
    self._device.auth()
    self._schedule = schedule
    self._mixed_mode_heating_period = mixed_mode_heating_period

  def _get_on_cmd(self, hr=datetime.datetime.now().hour):
    if self._mode == Mode.Heat or \
            (self._mode == Mode.Mixed and \
             (hr in self._mixed_mode_heating_period)):
      return self._heating_cmd
    return self._cooling_cmd

  def turn_on(self):
    try:
      self._device.send_data(self._get_on_cmd())
      return True
    except:
      return False

  def turn_off(self):
    try:
      self._device.send_data(self._off_cmd)
      return True
    except:
      return False
  
  def should_be_on(self):
    return datetime.datetime.now().hour in self._schedule

  def time_tick(self):
    hr = datetime.datetime.now().hour
    if self._get_on_cmd(hr=hr-1) != self._get_on_cmd(hr=hr):
      self.turn_on()
      return True
    return False

gin.parse_config_file(os.path.join(
    str(Path.home()), '.autohome/broadlink_cfg.gin'))
