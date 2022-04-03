""" Control a minisplit via IR. """

import broadlink
import gin
import os
from pathlib import Path

@gin.configurable
class Minisplit:

  def __init__(self, cool_cmd, off_cmd):
    self._cool_cmd = cool_cmd
    self._off_cmd = off_cmd
    self._device = broadlink.discover()[0]
    self._device.auth()

  def turn_cooling(self):
    self._device.send_data(self._cool_cmd)
    return True

  def turn_off(self):
    self._device.send_data(self._off_cmd)
    return True

gin.parse_config_file(os.path.join(
    str(Path.home()), '.autohome/broadlink_cfg.gin'))
