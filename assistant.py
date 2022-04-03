"""Thermostat support via Google Assistant and Assistant Relay.

Get and install Assistant Relay (https://assistantrelay.com)

Set up a ~/.autohome/assistant.json:

{
  "username": "<The Assistant Relay username>",
  "url: "<Full Assitant Relay API URL, i.e. http://some.ip:3000/assistant>"
}
"""
import json
import requests
import os

from absl import flags
from pathlib import Path
from typing import Optional


DEFAULT_CFG_FILE = os.path.join(str(Path.home()), '.autohome/assistant.json')
_CFG = flags.DEFINE_string(
    'assistant_config', DEFAULT_CFG_FILE, 'configuration for assistant')


def _get_cfg_file(cfg_file:Optional[str]):
  cfg_file = cfg_file if cfg_file else _CFG.value
  with open(cfg_file) as f:
    return json.load(f)


def _tell(command:str, cfg_file:Optional[str]):
  cfg = _get_cfg_file(cfg_file)
  msg = dict(
      user=cfg['username'],
      command=command
    )
  
  response = requests.post(url=cfg['url'], json=msg)
  return response.ok

def turn_off(cfg_file:Optional[str]=None):
  return _tell(command='Turn off all thermostats', cfg_file=cfg_file)

def turn_on(cfg_file:Optional[str]=None):
  return _tell(command='Turn on all thermostats', cfg_file=cfg_file)