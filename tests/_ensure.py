# this file ensures tests work under pre-commit

import sys
from pathlib import Path

TEST_DIR = Path(__file__).resolve().parent
SRC_DIR = TEST_DIR.with_name("src")
sys.path.append(str(SRC_DIR))
