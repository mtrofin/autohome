"""Water heater support via Z-Wave.me
"""
import datetime
import device
import gin
import json
import requests
import os
import time

from pathlib import Path
from typing import List

_REPEATS = 5

@gin.configurable
class Waterheater(device.Device):

  def __init__(self, url:str, token:str, schedule:List[int]):
    super(Waterheater, self).__init__('waterheater')
    self._url = url
    self._session = requests.Session()
    self._session.headers.update({'Authorization':token})
    self._schedule = schedule

  def is_it_on(self):
    response = self._session.get(self._url)
    if not response.ok:
      return None
    data = json.loads(response.content)
    return data['data']['metrics']['level'] == 'on'
    

  def _switch_to(self, on:bool):
    url = self._url + '/command/' + ('on' if on else 'off')
    last_status = None
    for _ in range(_REPEATS):
      response = self._session.get(url)
      if not response.ok:
        time.sleep(1)
        continue
      last_status = self.is_it_on()
      if last_status:
        break
    return last_status == on
  
  def turn_on(self):
    return self._switch_to(True)

  def turn_off(self):
    return self._switch_to(False)

  def should_be_on(self):
    return datetime.datetime.now().hour in self._schedule


gin.parse_config_file(os.path.join(str(Path.home()), '.autohome/waterheater.gin'))
