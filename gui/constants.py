import os

# 기준 경로: 항상 gui/ 기준
BASE_DIR = os.path.dirname(__file__)
ICON_DIR = os.path.abspath(os.path.join(BASE_DIR, "../resources/icons"))

def icon(filename):
    return os.path.join(ICON_DIR, filename)