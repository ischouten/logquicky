# Hack for importing package beyond top-level
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import logquicky

log = logquicky.load('my-logger')

def run():
  log.info("And from here as well!")