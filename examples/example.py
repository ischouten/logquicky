#!/usr/bin/env python
import time

# Hack for importing package beyond top-level
import sys, os

sys.path.insert(1, os.path.join(sys.path[0], ".."))

import logquicky

# Create your logger.
log = logquicky.load("my-logger", level="DEBUG")

# Log
log.debug("Debug message")
time.sleep(0.5)

log.info("Info message")
time.sleep(0.5)

log.warning("Warning message")
time.sleep(0.7)

log.error("Error message")
time.sleep(0.4)

log.critical("Critical message")
time.sleep(0.6)

steps = 10
bar = logquicky.ProgressBar(steps=steps, fill="⬜", prefix="Loading steps...")

for i in range(0, steps):
    time.sleep(0.2)
    bar.update(i)

time.sleep(0.3)
log.info("All done. 🥳 ")

time.sleep(1)
