import os
import sys
import time

sys.path.insert(1, os.path.join(sys.path[0], ".."))

import logquicky
from logquicky.progressBar import ProgressBar

log = logquicky.load("log", level="INFO")
log.info("Loaded logger with info level")

bar = ProgressBar(10, "Loading...", fill="#", length=30)

if __name__ == "__main__":

    for i in range(1, 10):
        bar.update(i)
        time.sleep(1)
