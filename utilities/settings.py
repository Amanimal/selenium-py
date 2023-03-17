from pathlib import Path

# Build paths inside the project like this BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent

# Debug True is local and False is Docker
DEBUG = True
# True = GUI and False = headless
HEADLESS = True