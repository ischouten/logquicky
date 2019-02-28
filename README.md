# Logquicky

## Nicer python logging in one line

The python logging package from the standard library is awesome.
However, even hough setting it up takes just a few lines of code, configuring it to make it look nice across projects, just adds up to doing the same thing over and over.

Therefore, I created *logquicky*.

Because this is basically just a very simple configuration on the logging module, which also makes it very easy to fall back to it once you decide your project needs more advanced functionalities.
However, it hopes to save you some time when quickly building scripts or when getting started in a new project.

Finally, this is also my first (hopefully useful) little OpenSource software up on PyPI, so I figured it would be a good exercise.

## Features

- Colored log levels make it easy to identify different levels.
- Pre-configured formatting of log lines,
- Optional logging to a log file,
- Ability to rewrite lines for nicer progress bars etc.
- Based on Python's logging module.

## Installation

```bash
pip install logquicky
```

### Notes

logquicky is supported for python 3.6+ (due to usage of f-strings)

## How to use

### Quick example

```python
import logquicky

# Add this line to create your logger.
logger = logquicky.add('my-logger')

# Use this in every file where you want be able to log:
log = logquicky.get('my-logger')

# Log away!
log.info("Here is a log message")
```

### See it in action

![simple-example.svg](logquicky/res/simple-example.svg)