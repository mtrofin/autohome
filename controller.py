import device
import minisplit
import powerwall
import thermostat
import water_heater

from typing import List


def main():
  pw = powerwall.Powerwall()
  current_status = pw.is_power_on()
  device_types = [thermostat.Thermostat, minisplit.Minisplit, water_heater.Waterheater]
  for t in device_types:
    try:
      d = t()
      if current_status:
        d.power_is_on()
      else:
        d.power_is_off()
    except:
      d.log(device.ERROR, '!! Unhandled error !!')

if __name__ == '__main__':
  main()
