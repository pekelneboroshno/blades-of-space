import sys
from pathlib import Path

PROJECT_DIR = str(Path.cwd())
sys.path.append(PROJECT_DIR)
print(PROJECT_DIR)
