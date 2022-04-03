"""Thermostat support via Google Assistant and Assistant Relay.

Get and install Assistant Relay (https://assistantrelay.com)

"""
import device
import gin
import requests
import os

from pathlib import Path

@gin.configurable
class Thermostat(device.Device):

  def __init__(self, url:str, username:str):
    super(Thermostat, self).__init__('thermostat')
    self._url = url
    self._username = username


  def _tell(self, command:str):
    msg = dict(
        user=self._username,
        command=command
      )
    
    response = requests.post(url=self._url, json=msg)
    return response.ok

  def turn_off(self):
    return self._tell(command='Turn off all thermostats')
      
  def turn_on(self):
    return self._tell(command='Turn on all thermostats')


gin.parse_config_file(os.path.join(str(Path.home()), '.autohome/thermostat.gin'))
