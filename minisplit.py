""" Control a minisplit via IR. """

import broadlink
import device
import datetime
import gin
import os

from pathlib import Path
from typing import List

@gin.configurable
class Minisplit(device.Device):

  def __init__(self, on_cmd:bytes, off_cmd:bytes, schedule:List[int]):
    super(Minisplit, self).__init__('minisplit')
    self._on_cmd = on_cmd
    self._off_cmd = off_cmd
    self._device = broadlink.discover()[0]
    self._device.auth()
    self._schedule = schedule

  def turn_on(self):
    self._device.send_data(self._on_cmd)
    return True

  def turn_off(self):
    return self._device.send_data(self._off_cmd)
  
  def should_be_on(self):
    return datetime.datetime.now().hour in self._schedule


gin.parse_config_file(os.path.join(
    str(Path.home()), '.autohome/broadlink_cfg.gin'))
