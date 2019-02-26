import logquicky

# Add this line to create your logger.
logger = logquicky.add('my-logger')

# Use this in every file where you want be able to log:
log = logquicky.get('my-logger')

log.info("This is nicely formatted.")

log.warning("Warnings stand out!")