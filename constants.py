"""
core/constants.py

Shared constants used throughout XMRig Manager.
"""

from pathlib import Path


# -------------------------------------------------
# Application Information
# -------------------------------------------------

APP_NAME = "XMRig Manager"
APP_VERSION = "1.0.0"


# -------------------------------------------------
# Directory Paths
# -------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_DIR = BASE_DIR / "config"

LOG_DIR = BASE_DIR / "logs"

ASSETS_DIR = BASE_DIR / "assets"

THEMES_DIR = BASE_DIR / "themes"


# -------------------------------------------------
# Configuration Files
# -------------------------------------------------

SETTINGS_FILE = CONFIG_DIR / "settings.json"


# -------------------------------------------------
# Log Files
# -------------------------------------------------

APP_LOG_FILE = LOG_DIR / "xmrig-manager.log"

XMRIG_LOG_FILE = LOG_DIR / "xmrig.log"

XMRIG_ERROR_LOG_FILE = LOG_DIR / "xmrig-error.log"


# -------------------------------------------------
# Default XMRig API Settings
# -------------------------------------------------

DEFAULT_API_HOST = "127.0.0.1"

DEFAULT_API_PORT = 18088

DEFAULT_API_TOKEN = "xmrig-local-api"


# -------------------------------------------------
# Default Update Intervals
# -------------------------------------------------

DEFAULT_UPDATE_INTERVAL = 5

DEFAULT_LOG_REFRESH_INTERVAL = 1


# -------------------------------------------------
# XMRig Defaults
# -------------------------------------------------

DEFAULT_XMRIG_BINARY = "/opt/homebrew/bin/xmrig"

DEFAULT_CONFIG_FILE = (
    BASE_DIR /
    "config" /
    "xmrig.json"
)
