import device
import minisplit
import powerwall
import thermostat

from typing import List


def main():
  pw = powerwall.Powerwall()
  current_status = pw.is_power_on()
  devices:List[device.Device] = [thermostat.Thermostat(), minisplit.Minisplit()]
  for d in devices:
    if current_status:
      d.power_is_on()
    else:
      d.power_is_off()


if __name__ == '__main__':
  main()