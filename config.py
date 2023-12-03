import os
import sys
import logging
from pathlib import Path


try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
    BASE_DIR = sys._MEIPASS
except Exception:
    BASE_DIR = Path(__file__).parent

if sys.platform.startswith('win'):
    HOME_PATH = os.environ["HOMEPATH"]
else:
    HOME_PATH = os.environ["HOME"]

DESKTOP_PATH = os.path.join(HOME_PATH, 'Desktop')

if not os.path.exists(DESKTOP_PATH):
    DESKTOP_PATH = Path(sys.executable).parent

LOG_LEVEL = logging.DEBUG
LOG_FORMAT = '<%(name)s level: (%(levelname)s)> %(asctime)s: %(message)s'
LOG_DIR_PATH = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOG_DIR_PATH):
    os.mkdir(LOG_DIR_PATH)

LOG_FILE = os.path.join(LOG_DIR_PATH, 'app.log')
logging.basicConfig(filename=LOG_FILE, format=LOG_FORMAT, level=LOG_LEVEL)
