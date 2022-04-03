""" Detect grid status via Powerwall support.

The username and password are those set up as user (not installer) through
the powerwall internal web interface.
"""
import gin
import os

from typing import Optional
from pathlib import Path
from tesla_powerwall import Powerwall as PW
from tesla_powerwall.const import GridStatus

@gin.configurable
class Powerwall:

  def __init__(self, url:str, username:str, password:str):
    self._powerwall = PW(
      endpoint=url, timeout=20, verify_ssl=False, disable_insecure_warning=True)
    self._powerwall.login(password, username)

  def is_power_on(self) -> Optional[bool]:
    if not self._powerwall or not self._powerwall.is_authenticated():
      return None
    return self._powerwall.get_grid_status() == GridStatus.CONNECTED


gin.parse_config_file(os.path.join(str(Path.home()), '.autohome/powerwall.gin'))