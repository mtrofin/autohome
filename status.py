from pathlib import Path
import os

STATUS_DIR = os.path.join(str(Path.home()), '.autohome/status')

def get_cfg_path(config_name:str):
  return os.path.join(STATUS_DIR, config_name)

def get_status(config_name:str):
  p = get_cfg_path(config_name)
  if not os.path.exists(p):
    return None
  with open(p) as f:
    return bool(f.readline())

def set_status(config_name:str, v:bool):
  fname = get_cfg_path(config_name)
  os.makedirs(os.path.dirname(fname), exist_ok=True)
  with open(fname, 'w') as f:
    f.writelines([str(v)])