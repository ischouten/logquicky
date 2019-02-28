#!/usr/bin/env python

# Hack for importing package beyond top-level
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import logquicky

import example2_other_file

# Creates a new logger and returns it.
log = logquicky.create('my-logger')

log.info("I can log from here...")

example2_other_file.run()