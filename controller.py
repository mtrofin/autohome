import device
import minisplit
import powerwall
import thermostat
import water_heater

from typing import List


def main():
  pw = powerwall.Powerwall()
  current_status = pw.is_power_on()
  devices: List[device.Device] = [thermostat.Thermostat(), minisplit.Minisplit(), water_heater.Waterheater()]
  for d in devices:
    try:
      if current_status:
        d.power_is_on()
      else:
        d.power_is_off()
    except:
      d.log(device.ERROR, '!! Unhandled error !!')

if __name__ == '__main__':
  main()