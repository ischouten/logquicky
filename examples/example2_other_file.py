import logquicky

# Hack for importing package beyond top-level
import sys, os

sys.path.insert(1, os.path.join(sys.path[0], ".."))

log = logquicky.load("my-logger")


def run():
    log.info("And from here as well!")

