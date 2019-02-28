import time
import logquicky

# Create your logger.
logger = logquicky.add('my-logger', level="DEBUG")

# Enable writing to your logger
log = logquicky.get('my-logger')

# Log!
log.debug("Debug message")
time.sleep(0.5)

log.info("Info message")
time.sleep(0.5)

log.warning("Warnings message.")
time.sleep(0.7)

log.error("Error message")
time.sleep(0.4)

log.critical("Critical message")
time.sleep(0.6)