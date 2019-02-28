# Logquicky

## Nicer python logging in one line

The python logging package from the standard library is awesome.
However, even hough setting it up takes just a few lines of code, configuring it to make it look nice accross projects, just adds up to doing the same thing over and over.

Therefore, I created *logquicky*.

Because its basically just a very simple configuration on the logging module, which also makes it very easy to fall back to it once you decide your project needs more advanced functionalities.
However, it hopes to save you some time when quickly building scripts or when getting started in a new project.

Finally, this is also my first (hopefully useful) little OpenSource software up on PyPI, so I figured it would be a good exercise.

## Features

- Colored log levels make it easy to identify different levels.
- Better formatted log lines,
- Optional logging to standard-out, a log file,
- Ability to rewrite lines for nicer progress bars etc.
- Based on Python's logging module.
- Renames log level warning to 'WARN' in output for better readability.

## Installation

```bash
pip install logquicky
```

## How to use

Note: logquicky is supported for python 3.6+ (due to usage of f-strings)

### Quick example

```python
import logquicky

# Add this line to create your logger.
logger = logquicky.add('my-logger')

# Use this in every file where you want be able to log:
log = logquicky.get('my-logger')

log.info("This is nicely formatted.")

log.warning("Warnings stand out!")
```

### See it in action

![res-example/example.svg](res-example/example.svg)