""" Detect grid status via Powerwall support.

Create a ~/.autohome/powerwall.json config;
{
  "url":"<the powerwall url, e.g. https://powerwall>",
  "username":"<your email>",
  "password":"<password>"
}

Where the username and password are those set up as user (not installer) through
the powerwall internal web interface.
"""
import json
import os

from typing import Optional
from pathlib import Path
from tesla_powerwall import User
from tesla_powerwall import Powerwall
from absl import flags

# We use the global for test - vscode's python support doesn't quite understand
# absltest, so we avoid needing to init the flags this way.
DEFAULT_CFG_FILE = os.path.join(str(Path.home()), '.autohome/powerwall.json')
_CFG = flags.DEFINE_string(
    'powerwall_config', DEFAULT_CFG_FILE, 'configuration for powerwall')


def _is_power_on(url: str, username: str, pwd: str)->Optional[bool]:
  powerwall = Powerwall(
    endpoint=url, timeout=20, verify_ssl=False, disable_insecure_warning=True)
  powerwall.login(pwd, username)
  if not powerwall.is_authenticated():
    return None
  status = powerwall.get_grid_status()
  return status == status.CONNECTED


def is_power_on(cfg_file:Optional[str]=None):
  cfg_file = cfg_file if cfg_file else _CFG.value
  with open(cfg_file) as f:
    cfg = json.load(f)
    return _is_power_on(cfg['url'], cfg['username'], cfg['password'])
